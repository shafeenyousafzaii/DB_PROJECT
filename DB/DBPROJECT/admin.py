from django.contrib import admin

# Register your models here.
from .models import Student,Course,Semester,StudentEnrolledInCourse,CoursesOfferedByStudent,CoursesTaughtByInstructor,Instructor,Service,Campus,ServicesUsedByStudent,Chatbot

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(StudentEnrolledInCourse)
admin.site.register(CoursesOfferedByStudent)
admin.site.register(CoursesTaughtByInstructor)
admin.site.register(Instructor)
admin.site.register(Service)
admin.site.register(Campus)
admin.site.register(ServicesUsedByStudent)
admin.site.register(Chatbot)
# Path: DB/DBPROJECT/views.py
