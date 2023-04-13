"""InternshipFinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Bank.account.accountView import AccountListView
from Bank.branch.branchView import BranchListView
from Bank.transactions.transactionsView import TransactionListView
from Bank.loan.loanView import LoanListView
from Bank.transferAmount.transferAmountView import TransferAmountListView
from Leads.views import LeadListView
from Bank.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('Branch',BranchListView.as_view() ),
    path('Branch<int:pk>',BranchListView.as_view() ),
    path('Acc',AccountListView.as_view() ),
    path('Acc/<int:pk>',AccountListView.as_view() ),
    path('Transactions',TransactionListView.as_view() ),
    path('Transactions/<int:pk>',TransactionListView.as_view() ),
    path('Loan',LoanListView.as_view() ),
    path('Loan/<int:pk>',LoanListView.as_view() ),
    path('TransferAmount',TransferAmountListView.as_view() ),
    path('TransferAmount/<int:pk>',TransferAmountListView.as_view() ),
    path('Lead',LeadListView.as_view()),
    path('Lead/<int:pk>',LeadListView.as_view())

]
