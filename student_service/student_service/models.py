from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Local User model for student service - mirrors auth service User"""
    ROLES = (
        ("admin", "Admin"),
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("parent", "Parent"),
        ("staff", "Staff"),
        ("ministry", "Ministry")
    )
    role = models.CharField(max_length=20, choices=ROLES, default="student")
    phone_number = models.CharField(max_length=20, blank=True, null=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile' )
    admission_number = models.CharField(max_length=20, unique=True)
    grade = models.CharField(max_length=10)
    curriculum = models.CharField(max_length=100, choices=[("CBC","CBC"),("British","British"),("8-4-4","8-4-4")])
    parent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
