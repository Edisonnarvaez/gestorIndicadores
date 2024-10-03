from django.db import models

from .macroprocess import MacroProcess
from users.models.user import User

class Process(models.Model):
    processId = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    creationDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    macroProcessId = models.ForeignKey(MacroProcess, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name