import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Stock
from ..serializers import StockSerializer

#initiate the APIClient app
client = Client()

class GetAllStocksTest(TestCase):
    """ Test module for GET all stocks API """

    def setUp(self):
        Stock.objects.create(
            name="Amazon", ticker="AMZN", market_cap=891063000000, eps=24.10)
        Stock.objects.create(
            name="Microsoft", ticker="MSFT", market_cap=1066000000000, eps=5.06)
        Stock.objects.create(
            name="Apple", ticker="AAPL", market_cap=950000000000, eps=11.78)
        Stock.objects.create(
            name="Verizon", ticker="VZ", market_cap=232719000000, eps=3.83)
        )
    
    def test_get_all_stocks(self):
        #get API response
        response = client.get(reverse('get_post_stocks'))
        #get data from db
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        

