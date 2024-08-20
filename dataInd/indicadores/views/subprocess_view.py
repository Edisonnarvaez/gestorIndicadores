from rest_framework import viewsets
from ..models import SubProcess
from ..serializers.subprocess_serializer import SubProcessSerializer

class SubProcessViewSet(viewsets.ModelViewSet):
    queryset = SubProcess.objects.all()
    serializer_class = SubProcessSerializer