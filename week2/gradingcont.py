name=input("enter name of student: ")
reg=input("enter reg of student: ")

math=int(input("enter marks: "))
eng=int(input("enter marks: "))
kisw=int(input("enter marks: "))

def grade(x):
    if x >= 80:
        return "A"
    elif x >= 60 and x < 80:
        return"B"
    elif x >= 40 and x <60:
        return "C"
    else:
         return "D"

a=math; b=eng; c=kisw
meanGrade=(a+b+c)/3

print('{} reg {} scored {} {} in math,{} {} in eng, & {} {} in kisw, overall grade is {}'.format(name,reg,math,grade(math),eng,grade(eng),kisw,grade(kisw),meanGrade,grade(meanGrade)))


subjects=dict()

NofSubjects=int(input('Enter no of subjects'))
for n in range(1, NofSubjects+1):
    subjectName=input("enter name of subject")
    score=int(input("enter score of subject"))
    subjects[subjectName]=score

print(subjects)

for k,v in subjects.items():
    print(k, getGrade(v))
    sum +=v
    print("meanGrade is", getmean(sum))