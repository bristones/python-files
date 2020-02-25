name=input("enter name of student: ")
reg=input("enter reg of student: ")

subjects=dict()

NofSubjects=int(input('Enter no of subjects'))
for n in range(1, NofSubjects+1):
    subjectName=input("enter name of subject")
    score=int(input("enter score of subject"))
    subjects[subjectName]=score

print(subjects)

def grade(x):
    if x >= 80:
        return "A"
    elif x >= 60 and x < 80:
        return"B"
    elif x >= 40 and x <60:
        return "C"
    else:
         return "D"

for k,v in subjects.items():
    print(k, grade(v))
    sum +=v
    print("meanGrade is", mean(sum))