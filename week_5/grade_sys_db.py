 
import mysql.connector
from subjects_mod import Subjects
from student_mod import Students
from gradingsystem import getGrade
from gradingsystem import getMeanScore
from school_mod import School


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
    #school = School(schoolName, schoolAddress)

    Cursor = mydbConnection.cursor()
    Cursor.execute("INSERT INTO School(SchoolName, SchoolAddress),VALUES(%m,%m)",(schoolName,schoolAddress))
    connection.commit()


# CREATE USER 'root'@'%' IDENTIFIED BY '12345678';

    noOfSubjects = int(input('Enter no. of subjects \n'))

    for s in range(1, noOfSubjects+1):
        subjects = []

        subjectName = input('enter name of subject \n')
        # {} \n'.format(subjectScore)))
        subjectScore = int(input('enter the score \n'))
        # create an instance of the subject
        Cursor = mydbConnection.cursor()
        Cursor.execute("INSERT INTO subjects(subjectName, subjectScore),VALUES(%a,%a)",(studentName, RegNo))
        connection.commit()

    # create an instance of a student
    Cursor = mydbConnection.cursor()
    Cursor.execute("INSERT INTO subjects(studentName, RegNo),VALUES(%b,%b)",(studentName, RegNo))
    connection.commit()

for stud in students:
    print("\nStudent Name: {} RegNo: {}, School: {}, Subjects: {}".format(stud.studentName, stud.regNo,
                                                                          stud.school.schoolName, len(stud.subjects)))
    for subject in subjects:
        print("\n{} {} Grade: {}".format(subject.subjectName,
                                         subject.subjectScore, getGrade(subjectScore)))





# print('*************END REPORT CARD ******')