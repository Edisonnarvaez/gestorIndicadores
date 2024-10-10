from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    nit = models.CharField(max_length=50)
    legalRepresentative = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    contactEmail = models.EmailField()
    foundationDate = models.DateField()
    status = models.BooleanField(default=True)  # Activo/Inactivo

    def __str__(self):
        return self.name
