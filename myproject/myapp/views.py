from ast import Pass
from http.client import responses
from django.shortcuts import render
from django.http import JsonResponse

from .models import Items
from .serializers import ItemsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from myproject.myapp import serializers

# Create your views here.

@api_view(['GET','POST'])
def items_list(request):
    if request.method=='GET':
        items=Items.objects.all()
        serializer= ItemsSerializers(items,many=True)
        # return JsonResponse({"items":serializer.data})
        return Response(serializer.data)


    if request.method=='POST':
        serializer=ItemsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def item_func(request,id):
    try:
        item=Items.objects.get(pk=id)
    except Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=ItemsSerializers(item)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=ItemsSerializers(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    elif request.method=='DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)