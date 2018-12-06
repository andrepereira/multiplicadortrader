from django.db import models



class EURUSD(models.Model):
    bid = models.FloatField(null=True, blank=True, default=None)
    ask = models.FloatField(null=True, blank=True, default=None)
    price = models.FloatField(null=True, blank=True, default=None)
    timestamp = models.IntegerField(null=True, blank=True, default=None)

class GBPJPY(models.Model):
    bid = models.FloatField(null=True, blank=True, default=None)
    ask = models.FloatField(null=True, blank=True, default=None)
    price = models.FloatField(null=True, blank=True, default=None)
    timestamp = models.IntegerField(null=True, blank=True, default=None)

class AUDUSD(models.Model):
    bid = models.FloatField(null=True, blank=True, default=None)
    ask = models.FloatField(null=True, blank=True, default=None)
    price = models.FloatField(null=True, blank=True, default=None)
    timestamp = models.IntegerField(null=True, blank=True, default=None)