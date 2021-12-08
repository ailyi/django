from django.db import models

# Create your models here.


class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    grades = models.CharField(max_length=100)
    average_grade = models.FloatField()
