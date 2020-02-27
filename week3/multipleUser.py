student=dict()
student['1']='Amy'
student['2']='Bebe'
student['3']='Cece'
student['4']='Dorine'

print(student['1'])
for a in student:
    print(student[a])

for v in student.values():
    print(v)

for k,v in student.items():
    print(k,v)

print(len(student)):