from django.urls import path, include
from companies.views.headquarters_view import HeadquartersViewSet
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'headquarters', HeadquartersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
