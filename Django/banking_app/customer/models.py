from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    id_number = models.CharField(max_length=10,unique=True)
    balance = models.FloatField()
    age = models.IntegerField()
    
    class Meta:
        db_table = 'tbl_customer'
        managed = True #flush or sync db
    
    
    def __str__(self):
        return self.name 