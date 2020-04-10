from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=10,unique=True)

    class Meta:
        db_table = 'staff'
        managed = True #flush or sync db
    
    def __str__(self):
        return self.name 