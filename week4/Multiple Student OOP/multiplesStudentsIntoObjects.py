# multiple students
from classStudent_mod import Student 
from subjects_mod import Subjects 
from student_mod import Students 
from gradingsystem import getGrade
from gradingsystem import getMeanScore

noOfStudents = int(input('Enter the no of students'))

student=[]
# input details for many students
for n in range(1,noOfStudents+1):
    studentName = input('Enter Name of Student \n')
    regNo = input('Enter Reg Number \n')
    studentClass = input('Enter Class \n')

    schoolName = input('Enter Name of Skul \n')
    schoolAddress = input('Enter Address of Skul \n')
    school=School(schoolName,schoolAddress)

    nofsubjects= int(input('Enter no. of subjects \n'))
   
    Subjects=[]
    for s in range(1,nofsubjects+1):
        subjectName=input('enter name of subject \n'.strip())
        subjectScore=int(input('enter the score \n')#{} \n'.format(subjectScore)))
        
        #create an instance of the subject 
        subjecto=subjects(subjectName,subjectScore)
        Subjects.append(subjecto)

    #create an instance of a student
    student=students(studentName,regNo,schoolName,subject)
    #print(student.name)
    #print(student.schoolName)
    students.append(student)

for stude in student1:
    print(stude.name,stude.schoolName,len(stude.subjects))
    for subject in subjects:
        print(subject.name,subject.score,'Grade',getgrade(subjectScore))






    

#print('************* REPORT CARD ******')
#for k,v in students.items():
 #   print('Name:',v['name'])
#  print('Reg No:',v['RegNo'])
 #   print('Class:',v['class'])
  #  totalMarks = 0
   # for subject,score in v['scores'].items():
    #    totalMarks += score
     #   print(subject,score,"GRADE :",getGrade(score))
    #print('MEAN SCORE :',getMeanScore(totalMarks,len(v['scores'])))

    #print('MEAN GRADE :',getGrade(getMeanScore(totalMarks,len(v['scores']))))


#print('*************END REPORT CARD ******')
