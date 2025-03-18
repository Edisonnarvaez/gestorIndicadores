"""
URL configuration for dataInd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
#from indicadores import urls as indicadores_url

from django.urls import path
from users.views.user_view import PasswordResetRequestView, PasswordResetConfirmView, UserViewSet

#from users.views import enable_2fa, get_2fa_qr, verify_2fa
from rest_framework.routers import DefaultRouter

# Router para UserViewSet
#router = DefaultRouter()
#router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('indicators.urls')), 
    path('api/', include('companies.urls')), 
    path('api/', include('users.urls')), 

    # Autenticación
    path('api/auth/', include('rest_framework.urls')),

    #path('api-auth/', include('rest_framework.urls')),
    #path('api-token-auth/', include('rest_framework.urls')),

    # Reset de contraseña
    #path('api/password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    #path('api/password-reset-confirm/<int:user_id>/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<int:user_id>/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

    #path("enable-2fa/", enable_2fa, name="enable_2fa"),
    #path("get-2fa-qr/", get_2fa_qr, name="get_2fa_qr"),
    #path("verify-2fa/", verify_2fa, name="verify_2fa"),

    # 2FA
    path("api/enable-2fa/", UserViewSet.as_view({'post': 'enable_2fa'}), name="enable_2fa"),
    path("api/disable-2fa/", UserViewSet.as_view({'post': 'disable_2fa'}), name="disable_2fa"),
    path("api/verify-2fa/", UserViewSet.as_view({'post': 'verify_2fa'}), name="verify_2fa"),

]
