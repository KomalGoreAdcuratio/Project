from django.contrib import admin
from .account.account import Account
from .branch.branch import Branch
from .transactions.transactions import Transactiona
from .loan.loan import Loan
from .transferAmount.transferAmount import TransferAmount
# Register your models here.
admin.site.register(Account)
admin.site.register(Branch)
admin.site.register(Transactiona)
admin.site.register(TransferAmount)
admin.site.register(Loan)