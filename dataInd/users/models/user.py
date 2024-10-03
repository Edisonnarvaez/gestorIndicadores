from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from companies.models.company import Company
from companies.models.department import Department
from .role import Role

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
    userId = models.CharField(max_length=100, primary_key=True)  # Clave primaria personalizada
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    creationDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    lastLogin = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    # Campos requeridos por AbstractBaseUser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'  # Define el campo usado para el login
    REQUIRED_FIELDS = ['email', 'firstName', 'lastName']  # Otros campos requeridos

    objects = UserManager()  # Asigna el manager personalizado

    def __str__(self):
        return self.username
