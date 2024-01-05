from django.db import models
from django.contrib import admin


class Item(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits = 22, decimal_places=2)
    currency = models.CharField(max_length=20)

    def __str__(self):
        return f"name: {self.name}; price: {self.price} {self.currency}"

admin.site.register(Item)
