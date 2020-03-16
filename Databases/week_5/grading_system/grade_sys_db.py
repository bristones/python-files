 
import mysql.connector
from subjects_mod import Subject
from student_mod import Students
from gradingsystem import getGrade
from gradingsystem import getMeanScore
from school_mod import School
from theFunctions import schoolIntoDatabase
from theFunctions import studentIntoDatabase
from theFunctions import subjectIntoDatabase

mydbConnection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="@5*Star123456",
    database="school"
)

noOfStudents = int(input('Enter the no of students'))

# input details for many students
for s in range(noOfStudents):
    students = []
    studentName = input('Enter Name of Student \n')
    regNo = input('Enter Reg Number \n')
    studentClass = input('Enter Class \n')

    schoolName = input('Enter Name of Skul \n')
    schoolAddress = input('Enter Address of Skul \n')
    school = School(schoolName, schoolAddress)
    #inserting school into a DB
    schoolIntoDatabase(school)

# CREATE USER 'root'@'%' IDENTIFIED BY '12345678';

    noOfSubjects = int(input('Enter no. of subjects \n'))

    for s in range(1, noOfSubjects+1):
        subjects = []
        subjectName = input('enter name of subject \n')
        subjectScore = int(input('enter the score \n'))
        subject= Subject(subjectName, subjectScore)
        subjects.append(subject)
        #inserting subjects into a DB
        subjectIntoDatabase(subject)
        
        
    # create an instance of a student
    student = Students(studentName,regNo,studentClass)
    students.append(student)
    # insert student to database
    studentIntoDatabase(student)

for stud in students:
    print("\nStudent Name: {}, RegNo: {}, class:{}, school:{}, Subjects: {}".format(stud.studentName, stud.regNo, stud.studentClass, schoolName,subjectName ))
    for subj in subjects:
        print("\n{} {} Grade: {}".format(subj.subjectName, subj.subjectScore, getGrade(subjectScore)))




# print('*************END REPORT CARD ******')