from django.db import models
from currency.models import Currency
from customer.models import Customer

# Create your models here.
class Account(models.Model):
    AccNo = models.CharField(max_length=20)
    AccType = models.CharField(max_length=10)
    currency_id=models.ForeignKey(Currency,on_delete=models.CASCADE,default=1)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
   
    
    class Meta:
        db_table = 'tbl_account'
        managed = True #flush or sync db
        
    def __str__(self):
        return self.AccNo