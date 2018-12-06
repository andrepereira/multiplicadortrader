from django.core.management.base import BaseCommand
from quotes.models import EURUSD, GBPJPY, AUDUSD
import matplotlib.pyplot as plt
from datetime import datetime
import pytz

class Command(BaseCommand):
    help = 'Make charts of forex quotes from DB'

    def handle(self, *args, **kwargs):
         
        eurusds = EURUSD.objects.order_by('timestamp')

        x = []
        y = []
        
        for eurusd in eurusds:
            x.append(datetime.utcfromtimestamp(eurusd.timestamp))
            y.append(eurusd.price)
            

        fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
        ax.plot(x, y)
        fig.savefig('blog/static/to.png')   # save the figure to file
        plt.close(fig)
