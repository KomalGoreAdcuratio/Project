from django.db import models
from django.core.exceptions import ValidationError
from Bank.account.account import Account
from django.shortcuts import get_object_or_404
def checkAccountNumber(data):
    try:
        get_object_or_404(Account, pk=data)
        return data
    except:
        raise ValidationError('Enter your Valid Account Number !!')
def checkAmount(data):
    if data>0:
        return data
    raise ValidationError('Amount must be greater than 0')
class Transactiona(models.Model):
    transactionId=models.AutoField(primary_key=True)
    accountNumber=models.CharField(max_length=10,validators=[checkAccountNumber])
    toAccountNumber=models.ForeignKey(Account,on_delete=models.CASCADE)
    
   
    amount=models.DecimalField(max_digits=100,decimal_places=2,validators=[checkAmount])
 #   time=models.DateTimeField(auto_now_add=True, blank=True)
    def save(self, *args, **kwargs):
        accOfTranferer=Account.objects.get(accountNumber=self.accountNumber)
        accOfGetter=Account.objects.get(accountNumber=self.toAccountNumber)
        if accOfTranferer.balance+1000<self.amount:
            raise ValidationError("LOW Balance !!!")
        else:
            accOfTranferer.balance-=self.amount
            accOfGetter.balance+=self.amount
            accOfGetter.save()
            accOfTranferer.save()
        super(Transactiona, self).save(*args, **kwargs)
    def delete(self,*args, **kwargs):
        accOfTranferer=Account.objects.get(accountNumber=self.accountNumber)
        accOfGetter=Account.objects.get(accountNumber=self.toAccountNumber)
        if accOfTranferer.balance+1000<self.amount:
            raise ValidationError("Can't revert LOW Balance !!!")
        else:
            accOfTranferer.balance+=self.amount
            accOfGetter.balance-=self.amount
            accOfGetter.save()
            accOfTranferer.save()
        super(Transactiona, self).delete(*args, **kwargs)
