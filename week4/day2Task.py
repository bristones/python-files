class Students:
    def __init__(self,name,regNo,studentClass):
        self.name=name 
        self.regNo=regNo
        self.studentClass=studentClass
    
    



Nofstudents=int(input('wako wangapi'))
studentsDetails=[]
for x in range(1,Nofstudents+1):
    student=Students(input("jina"),input("regno ni?"),input("ako class?"))
    studentsDetails.append(student)


print(studentsDetails)
    



#print(Students)
# print("Name:",studentsDetails.name,input("jina"),"RegNo:",studentDetails.regNo,input("regno ni?"),"Class",studentDetails.studentClass,input("ako class?"))

