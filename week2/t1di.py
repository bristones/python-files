students=dict()

NofStudents=int(input("enter no of students"))
for s in range(1, NofStudents+1):
    student=dict()
    subjects=dict()
    studentName=input("enter name of student: ")
    studentReg=input("enter reg of student: ")
    studentClass=int(input("enter class of student"))
    student['Name'] = studentName
    student['RegNo'] = studentReg
    student['Class'] = studentClass 
    students[studentReg] = student

    NofSubjects=int(input('Enter no of subjects'))
    for n in range(1, NofSubjects+1):
        subjectName=input("enter name of subject")
        score=int(input("enter score of subject"))
        subjects[subjectName]=score
        student['scores'] = subjects


def grade(x):
    if x >= 80:
        return "A"
    elif x >= 60 and x < 80:
        return"B"
    elif x >= 40 and x <60:
        return "C"
    else:
        return "D"


def meanGrade(scores,NofSubjects):
    return scores/NofSubjects
    
def schoolGrade(scores, NofStudents):
    return scores/NofStudents


#***********************RESULT COPY*************************

#print(student.items())

for k,v in students.items():
    print("Name:",v['Name'])
    print("Reg No.:",v['RegNo'])
    print("Class:",v['Class'])
    for subject,scores in v['scores'].items():
        scores += score
        print(subject,score,"Grade:",grade(scores))
    print('MEAN SCORE:',meanGrade(scores,len(v['Nofsubjectsscores'])))
    print('SCHOOL GRADE:',schoolGrade(scores,len(v['Nofstudents'])))

#************************* The END******************************

#print("School Grade {}".format(schoolGrade))