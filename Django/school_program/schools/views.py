from django.shortcuts import render,redirect
from .models import School
from students.models import Student

# Create your views here.
def schoolIndex(request):
    schools=School.objects.all()
    context={'schools': schools}
    return render(request,'schools/schools_list.html', context)

def school_detail(request, school_id):
    school_student = Student.objects.filter(school=school_id)
    context={'school_student': school_student}
    return render(request,'schools/detail.html', context) 

def add(request):
    if request.method =="POST":
        form =request.POST
        print(form)
        school= School()
        school.code = form['code']
        school.name = form['name']
        school.address = form['address']
        school.no_of_students = form['no_of_students']
        school.save()   #insert in database
        
        #give us a new id of the recorded item
        return redirect ('schools:detail', school.pk)
    return render(request, 'schools/add.html', {})