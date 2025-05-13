from django.db import models

from users.models.user import User
from .process import Process

class SubProcess(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    author = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    creationDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    process = models.ForeignKey(Process, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    

    def __str__(self):
        return self.name