from django.db import models

# Template Model
class Currency(models.Model):
    ticker = models.CharField(max_length=10)           # Name of the stock
    price = models.FloatField()                         # Opening stock price
    change = models.FloatField()                        # Closing stock price
    percentChange = models.FloatField()                     # Amount of sales

    def __str__(self):
        return self.ticker
