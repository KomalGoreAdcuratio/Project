### CLASS BASED API VIEW

from rest_framework.response import Response
from Bank.branch.branch  import Branch
from Bank.branch.branchSerializer import BranchSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import django_filters.rest_framework
import json
from django.shortcuts import get_object_or_404

class BranchListView(APIView):
    def get(self,request,pk=None):
        
        if pk==None:
            branches = Branch.objects.all()
            branchSerializer = BranchSerializer(branches, many=True)
            return Response(branchSerializer.data)
        else:
            branches = Branch.objects.filter(id=pk)
            branchSerializer = BranchSerializer(branches, many=True)
            return Response(branchSerializer.data)
    @csrf_exempt
    def post(self,request):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk):
        try:
            branch=Branch.objects.get(id=pk)
        except :
            return Response("Invalid ID !!")
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def patch(self, request,pk):
        try:
            branch=Branch.objects.get(id=pk)
        except :
            return Response("Invalid ID !!")
       
    #    print(branch)
        serializer = BranchSerializer(branch, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        if pk==None:
            return Response("Enter ID ")
        else:
            branches = get_object_or_404(Branch ,pk=pk)
            #branchSerializer = BranchSerializer(branches, many=True)
            branches.delete()
            return Response("Deleted !!!")
    

