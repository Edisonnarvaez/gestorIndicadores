from rest_framework import viewsets
from ..models import MacroProcess
from ..serializers.macroprocess_serializer import MacroProcessSerializer

class MacroProcessViewSet(viewsets.ModelViewSet):
    queryset = MacroProcess.objects.all()
    serializer_class = MacroProcessSerializer