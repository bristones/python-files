from django.db import models
from users.models import CustomUser

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    id_number = models.CharField(max_length=10,unique=True)
    address = models.CharField(max_length=20)
    age = models.IntegerField()
    pin = models.CharField(max_length=5)
    user = models.ForeignKey(CustomUser,default=1,null=False,on_delete=models.CASCADE)
    #address= models.CharField(max_length=25)
    
    class Meta:
        db_table = 'tbl_customers'
        managed = True #flush or sync db
    
    
    def __str__(self):
        return self.name 