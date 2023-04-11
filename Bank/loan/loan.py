from django.db import models
from Bank.account.account import Account
# Create your models here.

class Loan(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=25, choices=[('Home Loan','Home Loan'),
                                   ('Business Loan','Business Loan'),
                                   ('Personal Loan','Personal Loan'),
                                   ('Education Loan','Education Loan'),
                                   ('Vehicle Loan','Vehicle Loan'),
                                   ],default='Home Loan')
    amount=models.DecimalField( max_digits=10, decimal_places=2)
    intrestRate=models.DecimalField( max_digits=4, decimal_places=2)
    timeInYears=models.IntegerField()
    accountNumber=models.ForeignKey(Account,on_delete=models.CASCADE)
    
