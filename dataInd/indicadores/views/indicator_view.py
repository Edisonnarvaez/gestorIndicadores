from rest_framework import viewsets
from ..models import Indicator
from ..serializers.indicator_serializer import IndicatorSerializer

class IndicatorViewSet(viewsets.ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer