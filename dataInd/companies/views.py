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


#nuevo
from rest_framework import viewsets
from .models.company import Company
from .models.department import Department
from .serializers import CompanySerializer, DepartmentSerializer

# ViewSet para Company
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        """
        Sobrescribe el método para hacer filtros personalizados si es necesario.
        """
        queryset = Company.objects.all()
        # Puedes agregar lógica de filtrado aquí si es necesario
        return queryset

# ViewSet para Department
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        """
        Sobrescribe el método para hacer filtros personalizados si es necesario.
        """
        queryset = Department.objects.all()
        # Puedes agregar lógica de filtrado aquí si es necesario
        return queryset
