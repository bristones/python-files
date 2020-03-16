class Students:
    def __init__(self,name,regNo,studentClass):
        self.name=name 
        self.regNo=regNo
        self.studentClass=studentClass
    
    
   #def myOutput(self):


Nofstudents=int(input('wako wangapi'))
studentsDetails=[]
for x in range(1,Nofstudents+1):
    student=Students((name=input("jina")),(regNo=input("regno ni?")),(studentClass=input("ako class?")))
    studentsDetails.append(student)

for y in studentsDetails:
    print('Name:{} RegNo:{} Class:{}'.format(name,regNo,studentClass))

#the correctOne is down here. check for differences and learn
class Students:
    def __init__(self,name,regNo,studentClass):
        self.name=name 
        self.regNo=regNo
        self.studentClass=studentClass
    
    
   #def myOutput(self):


Nofstudents=int(input('wako wangapi'))
studentsDetails=[]
for x in range(1,Nofstudents+1):
    name=input("jina")
    regNo=input("regno ni?")
    studentClass=input("ako class?")

    student=Students(name, regNo, studentClass)
    #student=Students(input("jina"),input("regno ni?"),input("ako class?"))
    studentsDetails.append(student)

for y in studentsDetails:
    print('Name:{} RegNo:{} Class:{}'.format( name,regNo,studentClass))

