from rest_framework import viewsets
from ..models import Department
from ..serializers.department_serializer import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer