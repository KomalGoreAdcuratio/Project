### CLASS BASED API VIEW

from rest_framework.response import Response
from  Bank.transactions.transactions import Transaction
from Bank.transactions.transactionsSerializer import TransactionsSerializers
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import django_filters.rest_framework
from django.shortcuts import get_object_or_404
import json


class TransactionListView(APIView):
    def get(self,request,pk=None):
        if pk==None:
            transactions = Transaction.objects.all()  #filter(pk=pk)
            print(transactions)
            transactionsSerializer = TransactionsSerializers(transactions)
            return Response(transactionsSerializer.data)
          #  return Response("Enter Valid Account Number !!!! ")
        else:
            transactions = Transaction.objects.filter(accountNumber=pk)
            transactionsSerializer = TransactionsSerializers(transactions, many=True)
            return Response(transactionsSerializer.data)

    @csrf_exempt
    def post(self,request):
        serializer =  TransactionsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    def delete(self,request,pk=None):
        if pk==None:
            return Response("Enter ID ")
        else:
            account =get_object_or_404(Transaction, pk=pk)
            account.delete()
            return Response("Deleted !!!")
    

