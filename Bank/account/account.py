from Bank.branch.branch  import Branch
from django.db import models
from django.core.exceptions import ValidationError
#from .transactions import Transactions
def chechBalance(data):
    if data<1000:
        raise ValidationError("Min balance must be 1000")
def checkAccountNumber(data):
    if len(str(data))==10:
        return data
    raise ValidationError("Account number must be of 10 digit") 

def checkAadhareNumber(data):
    if len(str(data))==12:
        return data
    raise ValidationError("Aadhar Number must be of 12 digits !!!!")

class Account(models.Model):
   # id=models.CharField(max_length=20,default='xyz')
    accountNumber=models.CharField(max_length=10, primary_key=True,validators=[checkAccountNumber])
    branch_Id=models.ForeignKey(Branch,  on_delete=models.CASCADE,default=1)
   # transaction=models.OneToOneField(Transactions,blank=True)
    name=models.CharField(max_length=20)
 #   aadharCard=models.IntegerField(validators=[checkAadhareNumber],blank=True)
    type=models.CharField(max_length=10,choices=[('Saving','Saving'),('Current','Current'),('Minor','Minor')],default='Saving')
  #  contactNumber= models.IntegerField(blank=True)
    address=models.CharField(max_length=50, blank=True)
    balance=models.DecimalField( max_digits=100,default=10000.00, decimal_places=2 ,validators=[chechBalance])
    def __str__(self):
        return f"{self.accountNumber}"

