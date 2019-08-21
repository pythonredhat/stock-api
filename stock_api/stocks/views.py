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
        serializer = StockSerializer(stock)
        return Response(serializer.data)
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
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)
    #insert a new record for a stock
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'ticker': request.data.get('ticker'),
            'market_cap': int(request.data.get('market_cap')),
            'eps': float(request.data.get('eps'))
        }
        serializer = StockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

