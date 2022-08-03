from os import stat
from rest_framework.response import Response
from rest_framework.decorators import api_view
from renanBase.models import Product
from .serializers import ItemSerializer
from rest_framework import status



## to view all the items
@api_view(['GET'])
def getData(request):
    items = Product.objects.all()
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


## to view the single item details
@api_view(['GET'])
def item_detail(request, pk):
    items = Product.objects.filter(pk=pk)
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


## to create a new entry
@api_view(['POST'])
def postData(request):
   serializer = ItemSerializer(data=request.data)
   if serializer.is_valid():
    serializer.save()  
    return Response(serializer.data,status=status.HTTP_201_CREATED)


## to update data
@api_view(['PUT'])
def updateData(request,pk):
    items = Product.objects.filter(pk=pk).first()
    serializer = ItemSerializer(items, data=request.data)
    if serializer.is_valid():
        serializer.save()  
    return Response(serializer.data,status=status.HTTP_202_ACCEPTED)


## to delete data
@api_view(['DELETE'])
def deleteData(request,pk):
    items = Product.objects.get(pk=pk)
    serializer = ItemSerializer(items, data=request.data)
    items.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)    