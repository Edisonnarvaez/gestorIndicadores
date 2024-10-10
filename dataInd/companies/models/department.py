from django.db import models
from .company import Company

class Department(models.Model):
    name = models.CharField(max_length=255)
    departmentCode = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
    description = models.TextField()
    creationDate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)  # Activo/Inactivo

    def __str__(self):
        return self.name