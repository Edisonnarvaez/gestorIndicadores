from django.db import models

from .department import Department
from .user import User

class MacroProcess(models.Model):
    macroProcessId = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField()
    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    creationDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
