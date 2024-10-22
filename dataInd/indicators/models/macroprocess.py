from django.db import models

from companies.models.department import Department
from users.models.user import User

class MacroProcess(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    code = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    creationDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    

    def __str__(self):
        return self.name
