from rest_framework import serializers
from ..models.result import Result

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'