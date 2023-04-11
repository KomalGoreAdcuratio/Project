from rest_framework.response import Response
from  Bank.loan.loan import Loan
from Bank.loan.loanSerializer import LoanSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import django_filters.rest_framework
from django.shortcuts import get_object_or_404
import json

class LoanListView(APIView):
    def get(self,request,pk=None):
        
        if pk==None:
            loan= Loan.objects.all()
            loanSerializer = LoanSerializer(loan, many=True)
            return Response(loanSerializer.data)
        else:
            loan = Loan.objects.filter(accountNumber=pk)
            
            loanSerializer = LoanSerializer(loan, many=True)
            return Response(loanSerializer.data)
    @csrf_exempt
    def post(self,request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk=None):
       
        try:
            loan = get_object_or_404(Loan, pk=pk)
        except:
            return Response("Invalid ID !!")
       # print(account)
        serializer = LoanSerializer(loan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def patch(self, request,pk=None):
        try:
            loan = get_object_or_404(Loan, pk=pk)
        except:
            return Response("Invalid ID !!")
       
        serializer = LoanSerializer(loan, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        if pk==None:
            return Response("Enter ID ")
        else:
            loan =get_object_or_404(Loan, pk=pk)
            loan.delete()
            return Response("Deleted !!!")