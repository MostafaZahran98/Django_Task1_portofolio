from django.contrib import admin
from .models import Student,Course
# Register your models here.
#admin.site.register(Student)
#admin.site.register(Course)

class StudentAdmin(admin.ModelAdmin): 
	list_display = ("fullname", "Assigned_courses",)
admin.site.register(Student, StudentAdmin)



class CourseAdmin(admin.ModelAdmin): 
	list_display = ("coursename", "instructor_name",)
admin.site.register(Course, CourseAdmin)
