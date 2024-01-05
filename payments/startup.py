import stripe
from django.apps import AppConfig
from django.conf import settings # new
from . import models
import json

def main():
    stripe.api_key = settings.STRIPE_SECRET_KEY
    prices = [{'product_obj':stripe.Product.retrieve(i['product']), **i} for i in stripe.Price.list()['data']]
    models.Item.objects.all().delete()
    for i in prices:
        item = models.Item(name=i['product_obj']['name'], description=i['product_obj']['description'], price=i['unit_amount']/100, currency=i['currency'])
        item.save()