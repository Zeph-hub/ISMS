from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ("admin", "Admin"),
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("parent", "Parent"),
        ("staff", "Staff"),
        ("ministry", "Ministry")
    )
    role = models.CharField(max_length=20, choices=ROLES)
    phone_number = models.CharField(max_length=20, blank=True, null=True)