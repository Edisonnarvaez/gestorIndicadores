from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from companies.models.company import Company
from companies.models.department import Department
from .role import Role

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
            extra_fields['company'] = Company.objects.first()  # Asigna un valor por defecto
        if 'department' not in extra_fields:
            extra_fields['department'] = Department.objects.first()  # Asigna un valor por defecto
        if 'role' not in extra_fields:
            extra_fields['role'] = Role.objects.first()  # Asigna un valor por defecto

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):  # Agrega PermissionsMixin para soporte de permisos
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    creationDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    lastLogin = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    # Campos requeridos por AbstractBaseUser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'firstName', 'lastName']

    objects = UserManager()

    def __str__(self):
        return self.username

    # Métodos de permisos
    def has_perm(self, perm, obj=None):
        """Este método verifica si el usuario tiene un permiso específico."""
        return self.is_superuser or self.is_active

    def has_module_perms(self, app_label):
        """Este método verifica si el usuario tiene permiso para ver el módulo (aplicación) especificado."""
        return self.is_superuser or self.is_active
