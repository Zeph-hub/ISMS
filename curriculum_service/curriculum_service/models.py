from django.db import models
from django.contrib.auth.models import User

class subject(models.Model):
    name = models.CharField(max_length=100)
    curriculum = models.CharField(max_length=30, choices=[("CBC", "CBC"), ("8-4-4", "8-4-4"), ("British", "British Curriculum")])

class Assessment(models.Model):
    student_id = models.IntegerField() 
    subject = models.ForeignKey(subject, on_delete=models.CASCADE) 
    score = models.FloatField() 
    competency = models.CharField(max_length=100, blank=True, null=True) # CBC-specific 
    term = models.CharField(max_length=20)

    