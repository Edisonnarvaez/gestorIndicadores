from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from companies.models.company import Company
from companies.models.department import Department
from .role import Role
import pyotp

from django.utils.timezone import now
from datetime import timedelta

from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
import qrcode
from io import BytesIO



class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if 'company' not in extra_fields:
            extra_fields['company'] = Company.objects.first()  # Valor por defecto
        if 'department' not in extra_fields:
            extra_fields['department'] = Department.objects.first()  # Valor por defecto
        if 'role' not in extra_fields:
            extra_fields['role'] = Role.objects.first()  # Valor por defecto

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True, blank=True)
    creationDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    lastLogin = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)
    
    # Campos de autenticación
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # 2FA con OTP
    otp_secret = models.CharField(max_length=32, blank=True, null=True)
    otp_verified_at = models.DateTimeField(blank=True, null=True)  # Nuevo campo para rastrear verificación de 2FA
    otp_expires_at = models.DateTimeField(blank=True, null=True)  # Nuevo campo para expiración de OTP
    is_2fa_enabled = models.BooleanField(default=False)  # Nuevo campo para habilitar/deshabilitar 2FA
    otp_attempts = models.IntegerField(default=0)  # Contador de intentos fallidos
    otp_locked_until = models.DateTimeField(blank=True, null=True)  # Bloqueo temporal por intentos fallidos

    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'firstName', 'lastName']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser or self.is_active

    def has_module_perms(self, app_label):
        return self.is_superuser or self.is_active

    def generate_otp_secret(self):
        self.otp_secret = pyotp.random_base32()
        self.save()
        #self.send_2fa_email("Se ha generado un nuevo secreto OTP.")
    
    def get_totp_uri(self):
        return pyotp.TOTP(self.otp_secret).provisioning_uri(self.email, issuer_name="MiAppDataInd")

    def generate_otp_code(self):
        otp = pyotp.TOTP(self.otp_secret)
        self.otp_expires_at = now() + timedelta(minutes=5)
        self.otp_attempts = 0  # Reiniciar intentos fallidos
        self.otp_locked_until = None  # Desbloquear si estaba bloqueado
        self.save()
        return otp.now()

    def verify_otp(self, otp_code):
        if self.otp_locked_until and now() < self.otp_locked_until:
            return False  # Usuario bloqueado temporalmente

        #if self.otp_expires_at and now() > self.otp_expires_at:
        #    return False  # Código OTP expirado

        otp = pyotp.TOTP(self.otp_secret)
        if otp.verify(otp_code):
            self.otp_verified_at = now()
            self.otp_attempts = 0  # Reiniciar intentos fallidos
            self.otp_expires_at = None  # Invalidar OTP después de su uso
            self.save()
            return True
        
        self.otp_attempts += 1
        if self.otp_attempts >= 5:  # Bloquear después de 5 intentos fallidos
            self.otp_locked_until = now() + timedelta(minutes=5)
            self.send_2fa_email("Su cuenta ha sido bloqueada temporalmente por intentos fallidos de OTP.")
        self.save()
        return False

    #def send_2fa_email(self, message):
    #    send_mail(
    #        "Notificación de Autenticación en Dos Pasos",
    #        message,
    #        settings.DEFAULT_FROM_EMAIL,
    #        [self.email],
    #        fail_silently=False,
    #    )


    def send_2fa_email(self, message, otp_secret=None, otp_uri=None, enabled=True):
        subject = "Autenticación en Dos Pasos Activada" if enabled else "Autenticación en Dos Pasos Desactivada"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [self.email]

        # Renderizar contenido HTML
        context = {
            "message": message,
            "otp_secret": otp_secret,
            "enabled": enabled,
        }

        #print("otp_secret:", otp_secret)
        #print("otp_uri:", otp_uri)

        html_content = render_to_string("emails/2fa_email.html", context)

        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=from_email,
            to=to_email,
        )
        email.attach_alternative(html_content, "text/html")

        # Adjuntar QR solo si hay URI
        if otp_uri:
            qr = qrcode.make(otp_uri)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            buffer.seek(0)

            image = MIMEImage(buffer.read())
            image.add_header("Content-ID", "<qr_code>")
            image.add_header("Content-Disposition", "inline", filename="qr_code.png")
            email.attach(image)
        
        # 👉 Adjuntar logo como imagen embebida
        import os  # Asegúrate de tener esta importación al inicio del archivo
        logo_path = os.path.join(settings.BASE_DIR, "users", "templates", "assets", "logoslogan.png")
        if os.path.exists(logo_path):
            with open(logo_path, 'rb') as f:
                logo_image = MIMEImage(f.read())
                logo_image.add_header("Content-ID", "<logo_image>")
                logo_image.add_header("Content-Disposition", "inline", filename="logo.png")
                email.attach(logo_image)

        email.send(fail_silently=False)
