from django.shortcuts import render
from .models import Subject
from students.models import Student


# Create your views here.
def index(request):
    subjects = Subject.objects.all()
    context = {'subjects':subjects}
    return render(request, 'subjects/subject_lists.html', context)

def subject_index(request,pk):
    school_subjects = Subject.objects.get(pk=pk)  
    context = {'school_subjects': school_subjects}
    return render(request,"subjects/subject_details.html",context)

def add(request):
    if request.method =="POST":
        form =request.POST
       # print(form)
        subject= Subject()
        subject.subject_name = form['subject_name']
        subject.score = form['score']
        subject.student = Student.objects.get(pk=form['student'])   #foreign key
        subject.save()   #insert in database       
        #give us a new id of the recorded item
        return redirect('subject:index') #redirect to the link under urls.py

    students = Student.objects.all()  #gives options of the students
    context={'students':students}
       
    return render(request, 'subjects/add.html', context)