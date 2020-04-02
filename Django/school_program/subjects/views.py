from django.shortcuts import render
from .models import Subject
from students.models import Student


# Create your views here.
def index(request):
    subjects = Subject.objects.all()
    context = {'subjects':subjects}
    return render(request, 'subjects/subject_lists.html', context)

def single_student_subject(request,student_id):
    all_student_subjects = Subject.objects.filter(student=student_id)
    student_name = Student.objects.filter(pk=student_id)
    context = {'all_student_subjects':all_student_subjects,'student_name':student_name}
    return render(request,"subjects/subject_details.html",context)