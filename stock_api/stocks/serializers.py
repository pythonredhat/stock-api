from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('name', 'ticker', 'market_cap', 'eps', 'created_at', 'updated_at')


