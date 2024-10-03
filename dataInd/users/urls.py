from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views.role_view import RoleViewSet
from users.views.user_view import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
