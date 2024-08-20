from django.db import models

from .subprocess import SubProcess
from .user import User

class Indicator(models.Model):
    indicatorId = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    calculationMethod = models.TextField()
    measurementUnit = models.CharField(max_length=255)
    numerator = models.TextField()
    numeratorResponsible = models.CharField(max_length=255)
    numeratorSource = models.CharField(max_length=255)
    numeratorDescription = models.TextField()
    denominator = models.TextField()
    denominatorResponsible = models.CharField(max_length=255)
    denominatorSource = models.CharField(max_length=255)
    denominatorDescription = models.TextField()
    target = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    creationDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    subProcessId = models.ForeignKey(SubProcess, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    measurementFrequency = models.CharField(max_length=50)

    def __str__(self):
        return self.name
