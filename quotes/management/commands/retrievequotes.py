from django.core.management.base import BaseCommand
from quotes.models import EURUSD, GBPJPY, AUDUSD
import requests

class Command(BaseCommand):
    help = 'Retrieve forex quotes to DB'

    def handle(self, *args, **kwargs):
         
        r = requests.get('https://forex.1forge.com/1.0.3/quotes?pairs=EURUSD,GBPJPY,AUDUSD&api_key=vMO2pxqHkyOHxDdmyMWq0QM6YabLbmsq')

        response = r.json()

        eurusd = EURUSD(bid=response[0]['bid'], ask=response[0]['ask'], price=response[0]['price'], timestamp=response[0]['timestamp'])
        eurusd.save()

        gbpjpy = GBPJPY(bid=response[1]['bid'], ask=response[1]['ask'], price=response[1]['price'], timestamp=response[1]['timestamp'])
        gbpjpy.save()

        audusd = AUDUSD(bid=response[2]['bid'], ask=response[2]['ask'], price=response[2]['price'], timestamp=response[2]['timestamp'])
        audusd.save()