from django.contrib import admin
from .account.account import Account
from .branch.branch import Branch
from .transactions.transactions import Transaction
from .loan.loan import Loan
from .transferAmount.transferAmount import TransferAmount
from django_celery_results.models import *
# Register your models here.
admin.site.register(Account)
admin.site.register(Branch)
admin.site.register(Transaction)
admin.site.register(TransferAmount)
admin.site.register(Loan)