import mysql.connector
from school_mod import School

def getGrade(marks):
    if marks >= 80 and marks <= 100:
        return 'A'
    elif marks >= 60 and marks <80:
        return 'B'
    elif marks >= 40 and marks < 60:
        return 'C'
    elif marks >= 0 and marks < 40:
        return 'D'
    else:
        return 'Unknown Grade'


def getMeanScore(score):
    return score/3

def getSum(a,b,c):
    return a+b+c

#Establish the DB connection
def Connection():
    mydbConnection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="@5*Star123456",
    database="school"
    )
    return mydbConnection

#school function
def schoolIntoDatabase(School):
    myDbConnection=Connection()
    my_sql = "insert into school(schoolName, schoolAddress) Values(%s,%s)"
    val = (School.schoolName,School.schoolAddress)
    mycursor=myDbConnection.cursor()
    mycursor.execute(my_sql, val)
    myDbConnection.commit()
    print(mycursor.rowcount, "entry recorded to school Table.")
    
    #establishing the unique identifyer
    # regNo



#student function
def studentIntoDatabase(student):
    myDbConnection = Connection()
    my_sql = "insert into student(studentname, regNo, studentClass) Values(%s,%s,%s)"
    val = (student.studentName,student.regNo,student.studentClass)
    mycursor=myDbConnection.cursor()
    mycursor.execute(my_sql, val)
    myDbConnection.commit()
    print(mycursor.rowcount,"entry recorded to student Table.")

#subject function
def subjectIntoDatabase(subject):
    myDbConnection = Connection()
    my_sql = "insert into subjects(subjectName, subjectScore)Values(%s,%s)"
    val = (subject.subjectName, subject.subjectScore)
    mycursor=myDbConnection.cursor()
    mycursor.execute(my_sql, val)
    myDbConnection.commit()
    print(mycursor.rowcount, "entry recorded to subjects Table")

    