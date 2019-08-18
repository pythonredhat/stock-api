from django.db import models

class Stock(models.Model):
    """
    Stock Model
    Defines the attributes of a stock
    """

    name = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255)
    market_cap = models.IntegerField()
    eps = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_stock(self):
        return self.name + ' is worth ' + self.market_cap
    
    def __repr__(self):
        return self.name + ' is added.'
