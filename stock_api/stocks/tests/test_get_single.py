import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Stock
from ..serializers import StockSerializer

#initiate the APIClient app
client = Client()

class GetSingleStockTest(TestCase):
    """ Test module for GET single stock API """
    
    def setUp(self):
        self.amazon = Stock.objects.create(
            name="Amazon", ticker="AMZN", market_cap=891063000000, eps=24.10)
        self.microsoft = Stock.objects.create(
            name="Microsoft", ticker="MSFT", market_cap=1066000000000, eps=5.06)
        self.apple = Stock.objects.create(
            name="Apple", ticker="AAPL", market_cap=950000000000, eps=11.78)
        self.verizon = Stock.objects.create(
            name="Verizon", ticker="VZ", market_cap=232719000000, eps=3.83)

    def test_get_valid_single_stock(self):
        response = client.get(
            reverse('get_delete_update_stock', kwargs={'pk': self.amazon.pk}))
        stock = Stock.objects.get(pk=self.amazon.pk)
        serializer = StockSerializer(stock)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_stock(self):
        response = client.get(
            reverse('get_delete_update_stock', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
