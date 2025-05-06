from companies.serializers.company_serializer import CompanySerializer
from rest_framework import serializers
from companies.models.headquarters import Headquarters
from companies.serializers.department_serializer import DepartmentSerializer

class HeadquartersSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)  # Si deseas mostrar información de la compañía en las respuestas
    departament = DepartmentSerializer(read_only=True)  # Si deseas mostrar información de la compañía en las respuestas

    class Meta:
        model = Headquarters
        fields = ['id', 'habilitationCode','name', 'company', 'departament', 'city', 'address', 'habilitationDate', 'closingDate', 'status']

