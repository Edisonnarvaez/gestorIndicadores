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
from users.views.user_view import PasswordResetRequestView, PasswordResetConfirmView, UserViewSet
from rest_framework.routers import DefaultRouter


# con esta configuracion estaba funcioonando 
urlpatterns = [
    # Administración de Django
    path('admin/', admin.site.urls),

    # Endpoints de la API
    path('api/', include('indicators.urls')), 
    path('api/', include('companies.urls')), 
    path('api/', include('users.urls')), 

    # Autenticación con DRF
    path('api/auth/', include('rest_framework.urls')),


    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<int:user_id>/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

    # 2FA
    path("api/enable-2fa/", UserViewSet.as_view({'post': 'enable_2fa'}), name="enable_2fa"),
    path("api/disable-2fa/", UserViewSet.as_view({'post': 'disable_2fa'}), name="disable_2fa"),
    path("api/verify-2fa/", UserViewSet.as_view({'post': 'verify_2fa'}), name="verify_2fa"),

]
