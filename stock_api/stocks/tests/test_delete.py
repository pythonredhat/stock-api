import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Stock
from ..serializers import StockSerializer


#initiate the APIClient app
client = Client()

class DeleteSingleStockTest(TestCase):
    """ Test module for deleting an existing stock record """

    def setUp(self):
        self.amazon = Stock.objects.create(
            name="Amazon", ticker="AMZN", market_cap=891063000000, eps=24.10)
        self.microsoft = Stock.objects.create(
            name="Microsoft", ticker="MSFT", market_cap=1066000000000, eps=5.06)

    def test_valid_delete_stock(self):
        response = client.delete(
            reverse('get_delete_update_puppy', kwargs={'pk': self.amazon.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_stock', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)