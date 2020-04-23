from django.shortcuts import render
from .models import Student
from schools.models import School
from subjects.models import Subject

# Create your views here.
def index(request):
    student_details = Student.objects.all()
    context = {'student_data': student_details}
    return render(request, 'students/students_lists.html', context)

def student_detail(request, pk):
    #select * from students where student-id=x
    student = Student.objects.get(pk=pk)
    #select * from subjects where student_id=x
    subjects = Subject.objects.filter(pk=pk)
    
    context={'student': student, 'subjects':subjects}
    return render(request,'students/detail.html', context)

def add(request):
    if request.method =="POST":
        form =request.POST
        print(form)
        student= Student()
        student.name = form['code']
        student.registration_number = form['name']
        student.address = form['address']
        student.age = form['age']
        student.school = School.objects.get(pk=form['school'])
        student.save()   #insert in database 
               
        #give us a new id of the recorded item (use the appname and the viewnametag)
        return redirect ('student:student_list', student.pk)
    
    schools=School.objects.all()
    context={'schools':schools}
    
    
    return render(request, 'students/add.html', context)