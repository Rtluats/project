from django.db import models
from basket_app.models import Basket
from user_app.models import Customer, Restaurant, Courier
from product_app.models import Product
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from service_app.email_tasks import common
from django.urls import reverse
import copy
import collections


class Order(models.Model):
    class Status(models.IntegerChoices):
        WAIT = 1, "Wait"
        COOK = 2, "Cook"
        ON_THE_WAY = 3, "On the way"
        DELIVERED = 4, "Delivered"

    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.WAIT)
    end_price = models.DecimalField(max_digits=5, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer")
    is_canceled = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restaurant")
    products = models.ManyToManyField(Product)

    @property
    def owners(self):
        return [self.restaurant, self.customer]


@receiver(signal=pre_save, sender=Order)
def order_pre_save(sender, instance: Order, *args, **kwargs):
    """this method is necessary in order to divide the products by restaurants and form an order for the customer"""
    if instance.id is None:
        restaurant_products = {}
        for product in instance.products.all():
            if product.restaurant not in restaurant_products.keys():
                restaurant_products[product.restaurant] = [product]
            else:
                restaurant_products[product.restaurant].append(product)
        for restaurant in restaurant_products.keys():
            products = restaurant_products[restaurant]
            order = Order()
            order.restaurant = restaurant
            order.products = copy.deepcopy(products)
            order.customer = instance.customer
            products_count = collections.Counter()
            for product in products:
                products_count[product] += 1
            full_price = 0.0
            discount = 0.0
            for product in products_count.keys():
                for stock in product.stocks.all():
                    if stock.code == "1+1" and products_count[product] > 1:
                        discount += product.price - product.price * product.discount
                full_price += (product.price - product.price * product.discount) * products_count[product]
            order.end_price = full_price - discount
            order.save()


@receiver(signal=post_save, sender=Order)
def order_post_save(sender, instance, created, update_fields, *args, **kwargs):
    url_on_order = reverse("order-detail", kwargs={'pk': instance.id})
    if created:
        common.delay(url_on_order, instance.customer.email, "Заказ принят")
        common.delay(url_on_order, instance.restaurant.email, "Заказ принят")
    else:
        if "status" in update_fields:
            common.delay(url_on_order, instance.customer.email, f"Новый статус:{Order.Status.choices[update_fields['status']][1]}")
        if "is_canceled" in update_fields:
            common.delay(url_on_order, instance.customer.email, "Заказ отменён")
            common.delay(url_on_order, instance.restaurant.email, "Заказ отменён")