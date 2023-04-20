### CLASS BASED API VIEW

from rest_framework.response import Response
from .models import Leads
from .serializer import LeadSerializer
#from Bank.account.accountSerializer import AccountSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import django_filters.rest_framework
from django.shortcuts import get_object_or_404
#from Bank.account import Account
import json

class LeadListView(APIView):
    def get(self,request,pk=None):
        
        if pk==None:
            lead= Leads.objects.all()
            leadSerializer =LeadSerializer(lead, many=True)
            return Response(leadSerializer.data)
        else:
            print(pk)
            lead = Leads.objects.filter(leadNumber=pk)
            print(lead)
            leadSerializer = LeadSerializer(lead, many=True)
            
            return Response(leadSerializer.data)
    @csrf_exempt
    def post(self,request):
        serializer =LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def put(self, request,pk=None):
        try:
            lead=Leads.objects.get(leadNumber=pk)
        except :
            return Response("Invalid ID !!")
        serializer = LeadSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    
    def delete(self,request,pk=None):
        if pk==None:
            return Response("Enter ID ")
        else:
            branches = Leads.get_object_or_404( pk=pk)
            #branchSerializer = BranchSerializer(branches, many=True)
            branches.delete()
            return Response("Deleted !!!")
        
    # def patch(self, request,pk):
    #     try:
    #         lead=Leads.objects.get(leadNumber=pk)
    #     except :
    #         return Response("Invalid ID !!")
    #     dic={
    #     'accountNumber':lead.leadNumber,
    #     'name':lead.name
    
    
    #     }
    #     serializedData=AccountSerializer(data=dic)
    #     # serializedData.is_valid
    #     # print(serializedData.errors)
    #     # print(serializedData.error_messages)
    #     #return Response(serializedData.errors)
    #     if serializedData.is_valid():
    #         serializedData.save()
    #         return Response(serializedData.data)
    #     # return Response(serializedData.errors)
    
    def delete(self,request,pk=None):
        if pk==None:
            return Response("Enter ID ")
        else:
            lead =get_object_or_404(Leads, pk=pk)    
            lead.delete()
            return Response("Deleted !!!")
    

