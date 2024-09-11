from django.db import models

class Indicator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    process = models.ForeignKey('Process', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Process(models.Model):
    name = models.CharField(max_length=100)
    macroprocess = models.ForeignKey('MacroProcess', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SubProcess(models.Model):
    name = models.CharField(max_length=100)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Result(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    value = models.FloatField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.indicator.name} - {self.value}'

