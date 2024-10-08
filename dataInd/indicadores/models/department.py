from django.db import models

from .company import Company

class Department(models.Model):
    departmentId = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    departmentCode = models.CharField(max_length=50)
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    creationDate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name