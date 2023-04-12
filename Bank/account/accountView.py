### CLASS BASED API VIEW

from rest_framework.response import Response
from Bank.account.account import Account
from Bank.account.accountSerializer import AccountSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import django_filters.rest_framework
from django.shortcuts import get_object_or_404
import json


class AccountListView(APIView):
    def get(self,request,pk=None):
        if pk==None:
            account= Account.objects.all()
            accountSerializer = AccountSerializer(account, many=True)
            return Response(accountSerializer.data)
        else:
            print(pk)
            account = Account.objects.filter(accountNumber=pk)
            print(account)
            accountSerializer = AccountSerializer(account)
            return Response(accountSerializer.data)
    @csrf_exempt
    def post(self,request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk=None):
        try:
            account=Account.objects.get(accountNumber=pk)
        except :
            return Response("Invalid ID !!")
        
       # account = get_object_or_404(Account, pk=pk)
        
        #print(account)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def patch(self, request,pk):
        try:
            account=Account.objects.get(accountNumber=pk)
        except :
            return Response("Invalid ID !!")
        
        account = get_object_or_404(Account, pk=pk)
        
        print(account)
        serializer = AccountSerializer(account, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        if pk==None:
            return Response("Enter ID ")
        else:
            account =get_object_or_404(Account, pk=pk)
            account.delete()
            return Response("Deleted !!!")
    

