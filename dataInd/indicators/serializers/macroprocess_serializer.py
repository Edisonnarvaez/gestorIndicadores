from rest_framework import serializers
from ..models.macroprocess import MacroProcess

class MacroProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = MacroProcess
        fields = '__all__'