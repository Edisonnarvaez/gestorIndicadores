#from django.shortcuts import render
from rest_framework import viewsets
from .models import Indicator, Process, SubProcess, Result
from .serializers import IndicatorSerializer, ProcessSerializer, SubProcessSerializer, ResultSerializer

class IndicatorViewSet(viewsets.ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

class SubProcessViewSet(viewsets.ModelViewSet):
    queryset = SubProcess.objects.all()
    serializer_class = SubProcessSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

