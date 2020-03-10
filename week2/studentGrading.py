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


def meanScore(scores,NofSubjects):
    return totalMarks/NofSubjects
    
def schoolScore(scores, NofStudents):
    return totalMarks/NofStudents


#print("*"*15,"RESULT COPY", "*"*15)


for k,v in students.items():
    print("Name:",v['Name'])
    print("Reg No.:",v['RegNo'])
    print("Class:",v['Class'])
    totalMarks=0

    for subject,scores in v['scores'].items():
        totalMarks += score
        print(subject,score,grade(scores))
    print('MEAN SCORE:',meanScore(totalMarks,len(v['scores'])))

        print('MEAN GRADE:',grade(totalMarks,len(v['scores'])))

        print('SCHOOL GRADE:',schoolScore(totalMarks,len(v['scores'])))

        #print()

#print("*"*15,"THE END", "*"*15)

#print("School Grade {}".format(schoolGrade))