#students=['keysha', 'jay', 'kim', 'manie', 'apple', 'pie']
#print(students)
#print(students[5])  #printing one student, the last one
#print(students[-1], students[-2], students[-3])    #printing from backwards

#for n in students:
#    print(n)

#students[2]='Kimani'     #re assigning student 2 with another name
#print(students[2])

#for x in range(0,len(students)):     #listing all contents in the list- you have to loop and defing the lenght of the list
#    print(students[x])



#new task to create a list of studentsand output all names

#students.append('Kay','millie','josh','annie','melania','camila','ortiz','amy','barbie','cassie','dorthy','ellen','fancy','geog','honne','insta','jammie','kyle','lollie','mamie','nashville')
#newComers=('Kay','millie','josh','annie','melania','camila','ortiz','amy','barbie','cassie','dorthy','ellen','fancy','geog','honne','insta','jammie','kyle','lollie','mamie','nashville')

#students.append(newComers)
#print(students)

#students=[]

#newComers=int(input("number of students"))
#for n in range(0, newComers):
 #   newComersNames=input("the names of students")
  #  students.append(newComersNames)
    # /print(newComersNames)

#for x in range(0, len(students)):
 #   print(students[x])

list1=['Jan','feb','Mar','april']
list2=['may','june','july']
list3=list1+list2
#print(list3)

#list1.extend(list2)      
#print(list1)

#for loop also is a method of joining 2 lists      
for x in list2:
    list1.append(x)



list3.insert(1, "Aug")
print(list3)

print(list3[2:4])
print(list3[-4:-1])
print(list3[3:])
print(list3[:3])