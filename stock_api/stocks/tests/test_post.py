import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Stock
from ..serializers import StockSerializer

#initiate the APIClient app
client = Client()

class CreateNewStockTest(TestCase):
    """ Test module for inserting a new stock """

    def setUp(self):
        self.valid_payload = {
            'name': 'Amazon',
            'ticker': 'AMZN',
            'market_cap': 891063000000,
            'eps': 24.10
        }
        self.invalid_payload = {
            'name': '',
            'ticker': 'AMZN',
            'market_cap': 891063000000,
            'eps': 24.10
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('get_post_stocks'), 
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_stocks'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)