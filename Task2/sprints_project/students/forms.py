from django import forms
from .models import Student,Course

class MyForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ["fullname", "Assigned_courses",]
    labels = {'fullname': "Name", "Assigned_courses": "Assigned Courses",}
 
class MyForm1(forms.ModelForm):
  class Meta:
    model =Course
    fields = ["coursename", "instructor_name",]
    labels = {'coursename': "Course Name", "instructor_name": "Instructor Name",}
   