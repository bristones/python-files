from django.db import models


# Create your models here.
class Transactions(models.Model):
    recipient_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    amount = models.IntegerField()
    
    class Meta:
        db_table = 'tbl_transactions'
        managed = True #flush or sync db
    
    
    def __str__(self):
        return self.name 