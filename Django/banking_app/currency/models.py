from django.db import models

# Create your models here.
class Currency(models.Model):
    CurrName = models.CharField(max_length=10)
    CurrCode = models.IntegerField()
    
    


    class Meta:
        db_table = 'tbl_currency'
        managed = True #flush or sync db
        
    def __str__(self):
        return self.CurrName