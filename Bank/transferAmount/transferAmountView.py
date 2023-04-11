### CLASS BASED API VIEW

from rest_framework.response import Response
from Bank.transferAmount.transferAmount import TransferAmount
from Bank.transferAmount.transferAmountSerializer import TransferAmountSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import django_filters.rest_framework
from django.shortcuts import get_object_or_404
import json


class TransferAmountListView(APIView):
    def get(self,request,pk=None):
        
        if pk==None:
            transactions = TransferAmount.objects.all()  #filter(pk=pk)
            
            transactionsSerializer = TransferAmountSerializer(transactions, many=True)
            return Response(transactionsSerializer.data)
          #  return Response("Enter Valid Account Number !!!! ")
        else:
            transactions = TransferAmount.objects.filter(accountNumber=pk)
            
            transactionsSerializer = TransferAmountSerializer(transactions, many=True)
            return Response(transactionsSerializer.data)
    
    @csrf_exempt
    def post(self,request):
        serializer =  TransferAmountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    def delete(self,request,pk=None):
        if pk==None:
            return Response("Enter ID ")
        else:
            account =get_object_or_404(TransferAmount, pk=pk)
            account.delete()
            return Response("Deleted !!!")
    

