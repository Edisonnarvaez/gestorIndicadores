from rest_framework import viewsets
from ..models import Company
from ..serializers.company_serializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

