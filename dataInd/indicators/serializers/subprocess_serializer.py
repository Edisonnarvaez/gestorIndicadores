from rest_framework import serializers
from ..models.subprocess import SubProcess

class SubProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProcess
        fields = '__all__'