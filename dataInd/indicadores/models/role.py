from django.db import models

class Role(models.Model):
    roleId = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
