from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views.role_view import RoleViewSet
from users.views.user_view import UserViewSet, Toggle2FAView, RegenerateOTPSecretView, Verify2FAView, LoginView



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("login/", LoginView.as_view(), name="login"),
    path("2fa/toggle/", Toggle2FAView.as_view(), name="toggle-2fa"),
    path("2fa/verify/", Verify2FAView.as_view(), name="verify-2fa"),
    path("2fa/regenerate/", RegenerateOTPSecretView.as_view(), name="regenerate-otp-secret"),
]
