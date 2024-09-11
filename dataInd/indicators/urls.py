# indicators/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IndicatorViewSet, ProcessViewSet, SubProcessViewSet, ResultViewSet

router = DefaultRouter()
router.register(r'indicators', IndicatorViewSet)
router.register(r'processes', ProcessViewSet)
router.register(r'subprocesses', SubProcessViewSet)
router.register(r'results', ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
