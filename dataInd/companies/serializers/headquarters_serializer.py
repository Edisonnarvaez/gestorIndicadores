from companies.serializers.company_serializer import CompanySerializer
from rest_framework import serializers
from companies.models.headquarters import Headquarters

class HeadquartersSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)  # Si deseas mostrar información de la compañía en las respuestas
    #company_id = serializers.PrimaryKeyRelatedField(write_only=True,allow_null=True,queryset=company.objects.all(),source='company')

    class Meta:
        model = Headquarters
        fields = ['id', 'habilitationCode','name', 'company', 'departament', 'city', 'address', 'habilitationDate', 'closingDate', 'status']

