from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=200)
    Assigned_courses = models.CharField(max_length=200)

class Course(models.Model):
    coursename = models.CharField(max_length=255)
    instructor_name = models.CharField(max_length=255)    
# Create your models here.
