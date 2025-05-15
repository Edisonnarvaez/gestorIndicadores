from datetime import datetime
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import pyotp
from users.serializers.user_serializer import UserSerializer, LoginSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from email.mime.image import MIMEImage
import os
from django.conf import settings



User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_tokens_for_user(self, user):
        """Genera los tokens JWT para el usuario."""
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        """Autenticación con username y password. Si tiene 2FA activado, solicita el código OTP."""
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_2fa_enabled and user.otp_secret:  # Usa is_2fa_enabled
                    return Response(
                        {'message': 'Ingrese su código 2FA', 'user_id': user.id},
                        status=status.HTTP_200_OK
                    )
                
                tokens = self.get_tokens_for_user(user)
                return Response(tokens, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def verify_2fa(self, request):
        """Verifica el código 2FA y devuelve un token JWT."""
        user_id = request.data.get('user_id')
        otp_code = request.data.get('otp_code')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        if not user.otp_secret or not user.verify_otp(otp_code):
            return Response({'error': 'Código incorrecto o 2FA no activado'}, status=status.HTTP_400_BAD_REQUEST)
        
        tokens = self.get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)
    

    @action(detail=False, methods=['post'])
    def enable_2fa(self, request):
        """Habilita el 2FA generando una clave secreta para el usuario."""
        user = request.user
        user.generate_otp_secret()
        return Response({'message': '2FA activado', 'secret': user.otp_secret}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def disable_2fa(self, request):
        """Desactiva el 2FA eliminando la clave secreta."""
        user = request.user
        user.otp_secret = None
        user.save()
        return Response({'message': '2FA desactivado'}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get', 'put'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Obtiene o actualiza el perfil del usuario autenticado."""
        if request.method == 'GET':
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = UserSerializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def change_password(self, request):
        """Cambia la contraseña del usuario autenticado."""
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        if not current_password or not new_password:
            return Response({'error': 'Se requieren ambas contraseñas'}, status=status.HTTP_400_BAD_REQUEST)

        if not request.user.check_password(current_password):
            return Response({'error': 'Contraseña actual incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.set_password(new_password)
        request.user.save()
        return Response({'message': 'Contraseña actualizada'}, status=status.HTTP_200_OK)

class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = f"https://dataind.up.railway.app//password-reset-confirm/{user.pk}/{token}/"
            context = {
                'user': user,
                'reset_url': reset_url,
                'year': datetime.now().year
            }

            html_content = render_to_string("emails/password_reset.html", context)
            text_content = strip_tags(html_content)

            email_message = EmailMultiAlternatives(
                subject='Restablecimiento de contraseña',
                body=text_content,
                from_email='noreply@example.com',
                to=[email],
            )
            email_message.attach_alternative(html_content, "text/html")

            # Adjunta el logo con CID
            logo_path = os.path.join(settings.BASE_DIR, 'users', 'templates', 'assets', 'logoslogan.png')
            with open(logo_path, 'rb') as f:
                logo = MIMEImage(f.read())
                logo.add_header('Content-ID', '<logo_image>')
                logo.add_header('Content-Disposition', 'inline', filename='logoslogan.png')
                email_message.attach(logo)

            email_message.send()

            return Response({'message': 'Password reset link sent'}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, user_id, token):
        """Confirma el restablecimiento de contraseña y actualiza la nueva clave."""
        try:
            user = User.objects.get(pk=user_id)
            if PasswordResetTokenGenerator().check_token(user, token):
                new_password = request.data.get('new_password')
                if new_password:
                    user.set_password(new_password)
                    user.save()
                    return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
                return Response({'error': 'New password required'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({"error": "Credenciales inválidas."}, status=status.HTTP_401_UNAUTHORIZED)
        
        if user.is_2fa_enabled:
            otp_code = request.data.get("otp_code")
            if not otp_code:
                return Response({"message": "Se requiere código OTP."}, status=status.HTTP_206_PARTIAL_CONTENT)
            
            if not user.verify_otp(otp_code):
                return Response({"error": "Código OTP inválido o expirado."}, status=status.HTTP_400_BAD_REQUEST)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }, status=status.HTTP_200_OK)

class Verify2FAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        otp_code = request.data.get("otp_code")
        
        if not otp_code:
            return Response({"error": "Se requiere un código OTP."}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.verify_otp(otp_code):
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_200_OK)
        
        return Response({"error": "Código OTP inválido o expirado."}, status=status.HTTP_400_BAD_REQUEST)
    

class Toggle2FAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        enable_2fa = request.data.get("enable_2fa")

        if enable_2fa is None:
            return Response(
                {"error": "El parámetro 'enable_2fa' es requerido."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if enable_2fa:
            # Activar 2FA
            if not user.otp_secret:
                if hasattr(user, 'generate_otp_secret'):
                    user.generate_otp_secret()
                else:
                    user.otp_secret = pyotp.random_base32()

            user.is_2fa_enabled = True
            user.save()

            # SOLO aquí envías el correo con todo (secret + uri + QR)
            user.send_2fa_email(
                "La autenticación en dos pasos ha sido activada en su cuenta.",
                otp_secret=user.otp_secret,
                otp_uri=user.get_totp_uri(),
                enabled=True
            )

            return Response({
                'message': '2FA activado',
                'secret': user.otp_secret,
                'otp_uri': user.get_totp_uri()
            }, status=status.HTTP_200_OK)

        else:
            # Desactivar 2FA
            user.is_2fa_enabled = False
            user.otp_secret = ""
            user.save()

            # Enviar notificación de desactivación
            user.send_2fa_email(
                "La autenticación en dos pasos ha sido desactivada en su cuenta.",
                enabled=False
            )

            return Response({
                "is_2fa_enabled": user.is_2fa_enabled,
                "otp_secret": None,
                "message": "2FA desactivado"
            }, status=status.HTTP_200_OK)


class RegenerateOTPSecretView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        user.generate_otp_secret()
        user.save()
        return Response({
            "message": "Secreto OTP regenerado con éxito.",
            "otp_uri": user.get_totp_uri()
        }, status=status.HTTP_200_OK)
