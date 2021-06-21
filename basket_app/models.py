from django.db import models
from user_app.models import Customer
from product_app.models import Product
# Create your models here.


class Basket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    is_finished = models.BooleanField(default=False)