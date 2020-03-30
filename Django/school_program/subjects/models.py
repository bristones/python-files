from django.db import models

# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
   
    
    
class Meta:
        db_table = 'tbl_subject'
        managed = True #flush or sync db
        
def __str__(self):
    return self.subject_name