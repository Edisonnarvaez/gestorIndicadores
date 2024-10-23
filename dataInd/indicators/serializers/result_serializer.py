from rest_framework import serializers
from ..models.result import Result

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
        read_only_fields = ['calculatedValue']  # El valor calculado es de solo lectura
