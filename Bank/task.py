from celery import shared_task
import time
from  Bank.account.account import Account 
from Bank.branch.branch import Branch
from Bank.loan.loan import Loan
from Bank.transactions.transactions import Transaction
from Bank.transferAmount.transferAmount import TransferAmount
from faker import Faker
import random
import decimal





    
@shared_task
def dummyData():
    fake = Faker()
    n=20
    s=Branch.objects.all().delete()
    for i in range(1,n+1):
        s=Branch.objects.create(
            id=i,
            name=fake.name(),
            loc=fake.address()
        )
        s.save(using='default')
    n=100
    acc=Account.objects.all()
   
    BranchId=list(Branch.objects.values_list('id', flat=True))

    for i in range(1,n+1):
        typeOfAccount=['Saving','Current','Minor']
        s=Account.objects.create(
            accountNumber=1234467890+i,
            branch_Id= Branch.objects.get(id= random.choice(BranchId)) ,
            name=fake.name()[0:20],
            type=random.choice(typeOfAccount),
            address=fake.address(),
            balance=round(random.uniform(10000,100000000 ),2)
        )
        s.save(using='default')
    
    Id=list(Account.objects.values_list('accountNumber', flat=True))
    for i in range(1,n+1):
        typeOfLoan=choices=['Home Loan','Business Loan','Personal Loan','Education Loan','Vehicle Loan']
        Id=list(Account.objects.values_list('accountNumber', flat=True))                           
        s=Loan.objects.create(     
            accountNumber= Account.objects.get(accountNumber= str(random.choice(Id))) ,
            type=random.choice(typeOfLoan),
            amount=float(random.randrange(10000,1000000,100)),
            intrestRate=round(random.uniform(1,5),2),
            timeInYears=random.randrange(3,12),
            )
        s.save(using='default')
    n=100
    Id=list(Account.objects.values_list('accountNumber', flat=True))
    for i in range(1,n+1):              
        s=Transaction.objects.create(     
            accountNumber= random.choice(Id),
            toAccountNumber= Account.objects.get(accountNumber= str(random.choice(Id))),
            amount=random.randrange(10000,1000000,100),
        )
        if s.accountNumber!=s.toAccountNumber:
            try:
                s.save(using='default')
            except:
                pass
    n=50
    Id=list(Account.objects.values_list('accountNumber', flat=True))
    transationType=['Withdraw','Deposit']
    for i in range(1,n+1):              
        s=TransferAmount.objects.create(         
            accountNumber= Account.objects.get(accountNumber= str(random.choice(Id))),
            type=random.choice(transationType),
            amount=random.randrange(10000,1000000,100),
        )    
        if s.type=='Deposit':
            s.save(using='default')
        elif s.accountNumber.balance-s.amount>10000:
            s.save(using='default')
            
    
   
    
    
# from rest_framework import serializers


# class TransactionsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = '__all__'
#        # fields = '__all__'






# @shared_task
# def sleep20():
#     print('sleep start')
#     time.sleep(20)
#     print('sleep end')
    
# @shared_task
# def dummyBranchData(n=20):
#     fake = Faker()
#     s=Branch.objects.all().delete()
#     for i in range(1,n+1):
#         s=Branch.objects.create(
#             id=i,
#             name=fake.name(),
#             loc=fake.address()
#         )
#         s.save()

# @shared_task
# def dummyAccountData(n=200):
#     fake = Faker()
#     acc=Account.objects.all()
#     acc.delete()
#     BranchId=list(Branch.objects.values_list('id', flat=True))

#     for i in range(1,n+1):
#         typeOfAccount=['Saving','Current','Minor']
#         s=Account.objects.create(
#             accountNumber=1234467890+i,
#             branch_Id= Branch.objects.get(id= random.choice(BranchId)) ,
#             name=fake.name(),
#             type=random.choice(typeOfAccount),
#             address=fake.address(),
#             balance=round(random.uniform(10000,100000000 ),2)
#         )
#         s.save()

# @shared_task
# def dummyLoanData(n=50):
#     fake = Faker()
#     acc=Loan.objects.all()
#     acc.delete()
#     Id=list(Account.objects.values_list('accountNumber', flat=True))

#     for i in range(1,n+1):
#         typeOfLoan=choices=['Home Loan','Business Loan','Personal Loan','Education Loan','Vehicle Loan']
#         Id=list(Account.objects.values_list('accountNumber', flat=True))                           
#         s=Loan.objects.create(     
#             accountNumber= Account.objects.get(accountNumber= str(random.choice(Id))) ,
#             type=random.choice(typeOfLoan),
#             amount=float(random.randrange(10000,1000000,100)),
#             intrestRate=round(random.uniform(1,5),2),
#             timeInYears=random.randrange(3,12),
#             )
#         s.save()

# @shared_task
# def dummyTransactionData(n=50):
#     fake = Faker()
#     Id=list(Account.objects.values_list('accountNumber', flat=True))
#     for i in range(1,n+1):              
#         s=Transaction.objects.create(     
#             accountNumber= random.choice(Id),
#             toAccountNumber= Account.objects.get(accountNumber= str(random.choice(Id))),
#             amount=random.randrange(10000,1000000,100),
#         )
#         if s.accountNumber!=s.toAccountNumber:
            
#             s.save()
            


    
# @shared_task
# def dummyTransferData(n=50):
#     fake = Faker()
#     Id=list(Account.objects.values_list('accountNumber', flat=True))
#     transationType=['Withdraw','Deposit']
#     for i in range(1,n+1):              
#         s=TransferAmount.objects.create(     
            
#             accountNumber= Account.objects.get(accountNumber= str(random.choice(Id))),
#             type=random.choice(transationType),
#             amount=random.randrange(10000,1000000,100),
#         )    
#         s.save()
            
    
   
    
    