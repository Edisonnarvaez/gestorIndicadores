# indicators/serializers.py

from rest_framework import serializers
from .models import Indicator, Process, SubProcess, Result

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'

class SubProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProcess
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
