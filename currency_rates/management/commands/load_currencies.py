import json
import urllib2
from django.core.management.base import BaseCommand
from currency_rates.models import Currency

CURRENCIES_URL = "http://openexchangerates.org/currencies.json"


class Command(BaseCommand):
        help = "Load currencies from %s" % CURRENCIES_URL

        def handle(self, **options):

            f = urllib2.urlopen(CURRENCIES_URL)
            currencies = json.loads(f.read())

            for code, name in currencies.iteritems():
                Currency.objects.get_or_create(code=code, defaults={'name': name})
