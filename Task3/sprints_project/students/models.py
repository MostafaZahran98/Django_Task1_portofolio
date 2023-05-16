from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=200)
    Assigned_courses = models.CharField(max_length=200)
def __str__(self):
 return f"{self.fullname} {self.Assigned_courses}"    

class Course(models.Model):
    coursename = models.CharField(max_length=255)
    instructor_name = models.CharField(max_length=255)    
def __str__(self):
 return f"{self.coursename} {self.instructor_name}"    
# Create your models here.

