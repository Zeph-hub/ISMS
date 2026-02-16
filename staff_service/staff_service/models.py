from django.db import models
from django.contrib.auth.models import AbstractUser

class Staff(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    position = models.CharField(max_length=10)
    department = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    