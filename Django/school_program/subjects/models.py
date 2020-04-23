from django.db import models
from students.models import Student
from .grading_system import gradingSystem

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,default=1)
   
    
    class Meta:
        db_table = 'tbl_subject'
        managed = True #flush or sync db
            
    def __str__(self):
        return self.subject_name
    
    def ShowGrade(self):
        return gradingSystem(self.score)
    
    def __str__(self):
        return '{} {}' .fomart(self.name, self.showgrade())