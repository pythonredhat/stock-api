from django.shortcuts import render

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_stock(request, pk):
    try:
        stock = Stock.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #get details of a single stock
    if request.method == 'GET':
        return Response({})
    #delete a single stock
    elif request.method == 'DELETE':
        return Response({})
    #update details of a single stock
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_stocks(request):
    #get all stocks
    if request.method == 'GET':
        return Response({})
    #insert a new record for a stock
    elif request.method == 'POST':
        return Response({})

