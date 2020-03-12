# multiple students
from classStudent_mod import Student 
from subjects_mod import Subjects 
from gradingsystem import getGrade
from gradingsystem import getMeanScore

noOfStudents = int(input('Enter the no of students'))


# input details for many students
for n in range(1,noOfStudents+1):
    student=[]
    studentName = input('Enter Name of Student \n')
    regNo = input('Enter Reg Number \n')
    studentClass = input('Enter Class \n')

    schoolName = input('Enter Name of Skul \n')
    schoolAddress = input('Enter Address of Skul \n'
    school=School(schoolName,schoolAddress)

    nofsubjects= int(input('Enter no. of subjects \n'))
   
    
    for s in range(1,nofsubjects+1):
        subjects=[]
        subjectName=input('enter name of subject \n'.strip())
        subjectScore=int(input('enter the score \n')
        #create an instance of the subject 
        subject = Subject(subjectName,subjectScore)
        subjects.append(subject)

    #create an instance of a student
    student = Student(studentName,regNo,schoolName,subject)
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
