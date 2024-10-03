from rest_framework import serializers
from companies.models.company import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['companyId', 'name', 'nit', 'legalRepresentative', 'phone', 'address', 'contactEmail', 'foundationDate', 'status']

