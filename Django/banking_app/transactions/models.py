from django.db import models
from account.models import Account

# Create your models here.
class Transaction_type(models.Model): 
    type= models.CharField(max_length=10)
    trans_code= models.IntegerField()
    
    class Meta:
        db_table = 'T-Type'
        managed = True #flush or sync db
        
    def __str__(self):
        return self.type

class SendMoney(models.Model):
    recipient_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    amount = models.IntegerField()
    AccNo = models.ForeignKey(Account,on_delete=models.CASCADE,default=1)
    
    class Meta:
        db_table = 'sendMoney'
        managed = True #flush or sync db
        
    def __str__(self):
        return self.name
    
class Withdrawal(models.Model):
    amount = models.IntegerField()
    AccNo = models.ForeignKey(Account,on_delete=models.CASCADE,default=1)
    
    class Meta:
        db_table = 'withdraw'
        managed = True #flush or sync db
        
    def __str__(self):
        return self.amount
    
class Deposit(models.Model):
    amount = models.IntegerField()
    AccNo = models.ForeignKey(Account,on_delete=models.CASCADE,default=1)
    
    class Meta:
        db_table = 'deposit'
        managed = True #flush or sync db
    
    def __str__(self):
        return self.amount