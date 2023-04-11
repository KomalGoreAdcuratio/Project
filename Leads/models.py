from django.db import models
from django.core.exceptions import ValidationError
def chechBalance(data):
    if data<1000:
        raise ValidationError("Min balance must be 1000")
def checkAccountNumber(data):
    if len(str(data))==10:
        return data
    raise ValidationError("Account number must be of 10 digit") 

# Create your models here.
class Leads(models.Model):
    leadNumber=models.CharField(max_length=10, primary_key=True,validators=[checkAccountNumber])
    name=models.CharField(max_length=20)
    
 #   contactNumber= models.CharField(blank=True)
 
   
   