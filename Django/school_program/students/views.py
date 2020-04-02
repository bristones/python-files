from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    student_details = Student.objects.all()
    context = {'student_data': student_details}
    return render(request, 'students/students_lists.html', context)
