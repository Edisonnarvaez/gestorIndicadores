from django.db import models

from .indicator import Indicator
from .user import User

class Result(models.Model):
    resultId = models.CharField(max_length=100)
    numerator = models.FloatField()
    denominator = models.FloatField()
    calculatedValue = models.FloatField()
    creationDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    indicatorId = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    
    def calculateResult(self):
        self.calculatedValue = self.numerator / self.denominator

    def compareWithTarget(self, target: float):
        return self.calculatedValue >= target

    def __str__(self):
        return f"Result for {self.indicatorId.name}"