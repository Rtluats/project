from django.db import models

from user_app.models import Restaurant

# Create your models here.


class Stock(models.Model):
    code = models.CharField(max_length=300)
    description = models.TextField()

    @property
    def owner(self):
        return Product.objects.filter(stocks__id=self.id).first().restaurant


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    weight = models.DecimalField(max_digits=6, decimal_places=3)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    stocks = models.ForeignKey(Stock, on_delete=models.DO_NOTHING, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    @property
    def owner(self):
        return self.restaurant
