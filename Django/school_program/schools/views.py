from django.shortcuts import render,redirect
from .models import School
from students.models import Student
# from subjects.models import 

# Create your views here.
def schoolIndex(request):
    schools=School.objects.all()
    context={'schools': schools}
    return render(request,'schools/schools_list.html', context)

def school_detail(request, pk):
    #select * from schools where school_id=x
    school = School.objects.get(pk=pk)
    #select * from students where school_id=x
    students = Student.objects.filter(pk=pk)
    context= {
        'school':school, 
        'students':students,
        # 'subjects':subjects,
    }
    return render(request,'schools/detail.html', context) 


def add(request):
    if request.method =="POST":
        form =request.POST
        #print(form)
        school= School()
        school.code = form['code']
        school.name = form['name']
        school.address = form['address']
        school.no_of_students = form['no_of_students']
        school.save()   #insert in database
        
        #give us a new id of the recorded item
        return redirect('schools:school_detail', school.pk)
    return render(request, 'schools/add.html', {})