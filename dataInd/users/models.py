from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    # Campos adicionales si los necesitas, como company o department
    company = models.ForeignKey('companies.Company', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey('companies.Department', on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
