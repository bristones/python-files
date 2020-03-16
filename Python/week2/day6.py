
name=input("enter name of student")
reg=input("enter reg of student")
math=int(input("enter marks"))
eng=int(input("enter marks"))
kisw=int(input("enter marks"))

def marks(x):
    if x>=80:
        print("grade A")
    elif 60<x>80:
        print("grade B")
    elif 40<x<60:
        print("grade C")
    else:
         print("grade D")

marks=("grade")

print("{} of reg {} has grades{} in math, {} in eng, and {} in kisw.".format(name,reg,math,eng,kisw))

