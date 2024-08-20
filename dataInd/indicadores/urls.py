from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, RoleViewSet, DepartmentViewSet, UserViewSet, MacroProcessViewSet, ProcessViewSet, SubProcessViewSet, IndicatorViewSet, ResultViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'users', UserViewSet)
router.register(r'macroprocesses', MacroProcessViewSet)
router.register(r'processes', ProcessViewSet)
router.register(r'subprocesses', SubProcessViewSet)
router.register(r'indicators', IndicatorViewSet)
router.register(r'results', ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

