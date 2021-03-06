import collections
import copy

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse

from basket_app.models import Basket
from product_app.models import Product
from service_app.email_tasks import common
from user_app.models import Courier, Customer, Restaurant


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


# @receiver(signal=pre_save, sender=Order)
# def order_pre_save(sender, instance: Order,  *args, **kwargs):
#
#     if instance.id is None:
#         restaurant_products = {}
#         for product in Basket.objects.get(customer=instance.customer).products.all():
#             if product.restaurant not in restaurant_products.keys():
#                 restaurant_products[product.restaurant] = [product]
#             else:
#                 restaurant_products[product.restaurant].append(product)
#         for restaurant in restaurant_products.keys():
#             products = restaurant_products[restaurant]
#             order = Order.objects.create(customer=instance.customer, restaurant=restaurant)
#             order.products.set(products)
#             products_count = collections.Counter()
#             for product in products:
#                 products_count[product] += 1
#             full_price = 0.0
#             discount = 0.0
#             for product in products_count.keys():
#                 for stock in product.stocks.all():
#                     if stock.code == "1+1" and products_count[product] > 1:
#                         discount += product.price - product.price * product.discount
#                 full_price += (product.price - product.price * product.discount) * products_count[product]
#             order.end_price = full_price - discount
#             order.save()


@receiver(signal=post_save, sender=Order)
def order_post_save(sender, instance, created, update_fields, *args, **kwargs):
    url_on_order = reverse("order-detail", kwargs={'pk': instance.id})
    if created:
        common.delay(url_on_order, instance.customer.email, "?????????? ????????????")
        common.delay(url_on_order, instance.restaurant.email, "?????????? ????????????")
    else:
        if update_fields is not None:
            if "status" in update_fields:
                common.delay(url_on_order, instance.customer.email, f"?????????? ????????????:{Order.Status.choices[update_fields['status']][1]}")
            if "is_canceled" in update_fields:
                common.delay(url_on_order, instance.customer.email, "?????????? ??????????????")
                common.delay(url_on_order, instance.restaurant.email, "?????????? ??????????????")