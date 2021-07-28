import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.test import APIClient

from basket_app.models import Basket
from order_app.models import Order
from product_app.models import Product
from product_app.serializer import ProductSerializer
from user_app.models import Courier, Customer, Restaurant


@pytest.mark.django_db
def test_1():
    customer_json = {
      "username": "customer",
      "password": "customer",
      "email": "kosyrev-2000@mail.ru",
      "role": 1,
      "first_name": "aleks",
      "last_name": "kosyrev",
      "address": "string",
      "geolocation": "37.421925,-122.0841293"
    }
    customer_url_create = reverse("customer-list")
    client = APIClient()
    client.post(customer_url_create, customer_json, format="json")
    assert Customer.objects.count() == 1
    restaurant_json = {
      "username": "restaurant",
      "password": "restaurant",
      "email": "rtluats@gmail.com",
      "role": 2,
      "restaurant_name": "rtluats",
      "address": "string",
      "geolocation": "37.421925,-122.0841293"
    }
    restaurant_url_create = reverse("restaurant-list")
    client.post(restaurant_url_create, restaurant_json, format="json")
    assert Restaurant.objects.count() == 1
    client.force_authenticate(user=Restaurant.objects.all().first())
    product_json = {
        "id": "1",
        "name": "string",
        "description": "string",
        "weight": "25.00",
        "price": "100.00",
        "discount": "10.00",
        "stocks": None,
        "restaurant": Restaurant.objects.all().first().id
    }
    product_url_create = reverse("product-list")
    client.post(product_url_create, product_json, format="json")
    assert Product.objects.count() == 1
    basket_json = {
        "customer": Customer.objects.all().first().id,
        "products": [Product.objects.all().first().id,]
    }
    basket_url_create = reverse("basket-list")
    client.force_authenticate(user=Customer.objects.all().first())
    client.post(basket_url_create, basket_json, format="json")
    assert Basket.objects.count() == 1
    order_json = {
      "status": 1,
      "end_price": "0",
      "customer": Customer.objects.all().first().id,
      "is_canceled": False,
      "restaurant": Restaurant.objects.all().first().id,
      "products": [
          Product.objects.all().first().id
      ]
    }
    order_url_create = reverse("order-list")
    res = client.post(order_url_create, order_json, format="json")
    print(res)
    assert Order.objects.count() == 1
