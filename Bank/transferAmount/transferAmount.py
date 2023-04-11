from django.db import models
from django.core.exceptions import ValidationError
from Bank.account.account import Account
def checkAmount(data):
    if data>0:
        return data
    raise ValidationError('Amount must be greater than 0')
class TransferAmount(models.Model):
    transactionId=models.AutoField(primary_key=True)
    accountNumber=models.ForeignKey(Account,  on_delete=models.CASCADE)
   # accountNumber=models.ForeignKey(Account,default=1,on_delete=models.CASCADE)
    type=models.CharField(max_length=10,choices=[('Withdraw','Withdraw'),('Deposit','Deposit')],default='Deposit')
    amount=models.DecimalField(max_digits=100,decimal_places=2,validators=[checkAmount])
   # time=models.DateTimeField(auto_now_add=True, default=datetime.now)
    def save(self, *args, **kwargs):
        AccId=int(str(self.accountNumber).split(' ')[0])
        acc=Account.objects.get(accountNumber=AccId)
        if self.type=="Withdraw":
            diff=acc.balance-self.amount
            if diff>1000:
                acc.balance=acc.balance-self.amount
                acc.save()
            else:
                raise ValidationError("LOW Balance !!!")
        else:
            acc.balance+=self.amount
            acc.save()
        super(TransferAmount, self).save(*args, **kwargs)
    def delete(self,*args, **kwargs):
        AccId=int(str(self.accountNumber).split(' ')[0])
        acc=Account.objects.get(accountNumber=AccId)
        if self.type=="Deposit":
            diff=acc.balance-self.amount 
            if diff>1000:
                acc.balance=acc.balance-self.amount
                acc.save()
            else:
                raise ValidationError("LOW Balance !!!")
        else:
            acc.balance+=self.amount
            acc.save()
        super(TransferAmount, self).delete(*args, **kwargs)
