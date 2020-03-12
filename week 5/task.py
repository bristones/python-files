# multiple students
from subjects_mod import Subject
from student_mod import Student
from gradingsystem import getGrade
from gradingsystem import getMeanScore
from school_mod import School

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

    noOfSubjects = int(input('Enter no. of subjects \n'))

    for s in range(1, noOfSubjects+1):
        subjects = []

        subjectName = input('enter name of subject \n')
        # {} \n'.format(subjectScore)))
        subjectScore = int(input('enter the score \n'))
        # create an instance of the subject
        subject = Subject(subjectName, subjectScore)
        subjects.append(subject)

    # create an instance of a student
    student = Student(studentName, regNo, school, subjects)
    students.append(student)

for stud in students:
    print("\nStudent Name: {} RegNo: {}, School: {}, Subjects: {}".format(stud.studentName, stud.regNo,
                                                                          stud.school.schoolName, len(stud.subjects)))
    for subject in subjects:
        print("\n{} {} Grade: {}".format(subject.subjectName,
                                         subject.subjectScore, getGrade(subjectScore)))
                                         