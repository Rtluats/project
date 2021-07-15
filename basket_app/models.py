from django.db import models

from product_app.models import Product
from user_app.models import Customer


class Basket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    @property
    def owner(self):
        return self.customer
