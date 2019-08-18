from django.test import TestCase
from ..models import Stock

class StockTest(TestCase):
    """ Test module for Stock model"""

    def setUp(self):
        Stock.objects.create(
            name='Visa', ticker='V', market_cap=399306000000, eps=5.21)
        Stock.objects.create(
            name='Mastercard', ticker='MA', market_cap=278355000000, eps=6.48)

    def test_stock_worth(self):
        stock_visa = Stock.objects.get(name='Visa')
        stock_mastercard = Stock.objects.get(name='Mastercard')
        self.assertEqual(
            stock_visa.get_stock_value(), "Visa is worth 399306000000")
        self.assertEqual(
            stock_mastercard.get_stock_value(), 
        )
         