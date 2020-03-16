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
