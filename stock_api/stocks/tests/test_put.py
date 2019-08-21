import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Stock
from ..serializers import StockSerializer

#initiate the APIClient app
client = Client()

class UpdateSingleStockTest(TestCase):
    """ Test module for updating an existing stock record """

    def setUp(self):
        self.amazon = Stock.objects.create(
            name="Amazon", ticker="AMZN", market_cap=891063000000, eps=24.10)
        self.microsoft = Stock.objects.create(
            name="Microsoft", ticker="MSFT", market_cap=1066000000000, eps=5.06)
        self.valid_payload = {
            'name': 'Amazon',
            'ticker': 'AMZN',
            'market_cap': 891063000000,
            'eps': 24.10
        }
           self.invalid_payload = {
            'name': '',
            'ticker': 'AMZN',
            'market_cap': 89106384718903,
            'eps': 24.10
        }

    def test_valid_update_stock(self):
        response = client.put(
            reverse('get_delete_update_stock', kwargs={'pk': self.amazon.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_stock(self):
        response = client.put(
            reverse('get_delete_update_stock', kwargs={'pk': self.amazon.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)