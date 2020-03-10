from myfunctions import getMeanScore
from myfunctions import getGrade
from myfunctions import getSum
from mygrade_sys import grade

nameOfStudent= input('Enter name of student \n')
regNO=input('Enter the REG Number \n')
mathScore= int(input('Enter Math Score \n'))
engScore = int(input('Enter English Score \n'))
swaScore = int(input('Enter Swa Score \n'))

print('Exam Report for ',nameOfStudent,'\n')
print('MATH :',getGrade(mathScore),'\n')
print('ENG :',getGrade(engScore),'\n')
print('KISW :',getGrade(swaScore),'\n')
sum = getSum(mathScore,engScore,swaScore)
meanScore = getMeanScore(sum)
grade = getGrade(meanScore)

print('Mean Grade :',grade)
print('Mean Grade :',getGrade(getMeanScore(getSum(mathScore,engScore,swaScore))))