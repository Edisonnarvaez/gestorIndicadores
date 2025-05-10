from companies.serializers.company_serializer import CompanySerializer
from rest_framework import serializers
from companies.models.department import Department

class DepartmentSerializer(serializers.ModelSerializer):
    #company = CompanySerializer(read_only=True)  # Si deseas mostrar información de la compañía en las respuestas

    class Meta:
        model = Department
        fields = '__all__'# ['id', 'name', 'departmentCode', 'company', 'description', 'creationDate', 'status']

