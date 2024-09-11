#from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Department
from .serializers import CompanySerializer, DepartmentSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
