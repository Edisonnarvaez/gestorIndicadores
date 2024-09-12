from django.db import models

class Role(models.Model):
    roleId = models.CharField(max_length=100, primary_key=True)  # Clave primaria personalizada
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
