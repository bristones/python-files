from django.db import models
from account.models import Account
from account.models import Customer
from django.utils import timezone

# Create your models here.
class T_type(models.Model):
    tName = models.CharField(max_length=10)
    tCode = models.IntegerField()
    
    
    class Meta:
        db_table = 'transcType'
        managed = True #flush or sync db
        
    def __str__(self):
        return self.tName
    
# class All_transactions(models.Model): 
#     time = models.DateTimeField(default=timezone.now)
#     trans_code= models.IntegerField()
#     amount= models.FloatField()
#     balance= models.FloatField()
#     customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    
    class Meta:
        db_table = 'transactions'
        managed = True #flush or sync db
        
    def __str__(self):
        return self.trans_type

class SendMoney(models.Model):
    time = models.DateTimeField(default=timezone.now)
    trans_code= models.IntegerField()
    mobile = models.CharField(max_length=15)
    amount = models.IntegerField()
    balance= models.FloatField()
    AccNo = models.ForeignKey(Account,on_delete=models.CASCADE,default=1)
    
    
    class Meta:
        db_table = 'sendMoney'
        managed = True #flush or sync db
        
    def __str__(self):
        return self.name
    
class Withdrawal(models.Model):
    time = models.DateTimeField(default=timezone.now)
    trans_code= models.IntegerField()
    amount = models.IntegerField()
    balance= models.FloatField()
    AccNo = models.ForeignKey(Account,on_delete=models.CASCADE,default=1)
    
    class Meta:
        db_table = 'withdraw'
        managed = True #flush or sync db
        
    def __str__(self):
        return self.amount
    
class Deposit(models.Model):
    time = models.DateTimeField(default=timezone.now)
    trans_code= 2
    amount = models.IntegerField()
    balance= models.FloatField()
    AccNo = models.ForeignKey(Account,on_delete=models.CASCADE,default=1)
    
    class Meta:
        db_table = 'deposit'
        managed = True #flush or sync db
    
    def __str__(self):
        return self.amount