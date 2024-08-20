from rest_framework import viewsets
from ..models import Process
from ..serializers.process_serializer import ProcessSerializer

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer