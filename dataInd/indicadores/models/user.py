from django.db import models

from .company import Company
from .department import Department
from .role import Role

class User(models.Model):
    userId = models.CharField(max_length=100)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    creationDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    lastLogin = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.username