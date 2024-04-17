from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Course, Instructor
# Create your views here.
def index(request):
    return render(request, 'index.html')

def index(request):
    # Query the data from models
    student = Student.objects.first()
    course = Course.objects.first()
    instructor = Instructor.objects.first()

    # Pass the data to the template
    return render(request, 'index.html', {
        'student': student,
        'course': course,
        'instructor': instructor,
    })

# # In a view or anywhere else
# from django.urls import reverse

# url = reverse('DBPROJECT:index')
