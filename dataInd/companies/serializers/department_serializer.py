from rest_framework import serializers
from .models.department import Department

class DepartmentSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)  # Si deseas mostrar información de la compañía en las respuestas

    class Meta:
        model = Department
        fields = ['departmentId', 'name', 'departmentCode', 'companyId', 'description', 'creationDate', 'status']