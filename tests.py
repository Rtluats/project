import pytest
from user_app.models import Customer, Restaurant, Courier
from product_app.models import Product
from order_app.models import Order
from user_app.serializer import RestaurantSerializer
from basket_app.models import Basket
from django.urls import reverse
from rest_framework.test import APIClient
from mixer.backend.django import mixer


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
      "role": 1,
      "restaurant_name": "rtluats",
      "address": "string",
      "geolocation": "37.421925,-122.0841293"
    }
    restaurant_url_create = reverse("restaurant-list")
    client.post(restaurant_url_create, restaurant_json, format="json")
    assert Restaurant.objects.count() == 1
    product_json = {
        "name": "string",
        "description": "string",
        "weight": "25.00",
        "price": "100.00",
        "discount": "10.00",
        "stocks": [

        ],
        "restaurant": {
            "username": "restaurant",
            "password": "restaurant",
            "email": "rtluats@gmail.com",
            "role": 1,
            "restaurant_name": "rtluats",
            "address": "string",
            "geolocation": "37.421925,-122.0841293"
        }
    }
    product_url_create = reverse("product-list")
    client.force_authenticate(user=Restaurant.objects.all().first())
    client.post(product_url_create, product_json, format="json")
    assert Product.objects.count() == 1
    basket_json = {
        "customer": {
            "username": "customer",
            "password": "customer",
            "email": "kosyrev-2000@mail.ru",
            "role": 1,
            "first_name": "aleks",
            "last_name": "kosyrev",
            "address": "string",
            "geolocation": "37.421925,-122.0841293"
        },
        "products": [
            {
                "description": "string",
                "weight": "string",
                "price": "string",
                "discount": "string",
                "stocks": [

                ],
                "restaurant": {
                    "username": "restaurant",
                    "password": "restaurant",
                    "email": "rtluats@gmail.com",
                    "role": 1,
                    "restaurant_name": "rtluats",
                    "address": "string",
                    "geolocation": "37.421925,-122.0841293"
                }
            }
        ]
    }
    basket_url_create = reverse("basket-list")
    client.force_authenticate(user=Customer.objects.all().first())
    client.post(basket_url_create, basket_json, format="json")
    assert Basket.objects.count() == 1
    order_json = {
      "status": 1,
      "basket": {
        "customer": {
            "username": "customer",
            "password": "customer",
            "email": "kosyrev-2000@mail.ru",
            "role": 1,
            "first_name": "aleks",
            "last_name": "kosyrev",
            "address": "string",
            "geolocation": "37.421925,-122.0841293"
        },
        "products": [
            {
                "description": "string",
                "weight": "string",
                "price": "string",
                "discount": "string",
                "stocks": [

                ],
                "restaurant": {
                    "username": "restaurant",
                    "password": "restaurant",
                    "email": "rtluats@gmail.com",
                    "role": 1,
                    "restaurant_name": "rtluats",
                    "address": "string",
                    "geolocation": "37.421925,-122.0841293"
                }
            }
        ]
      },
      "end_price": "string",
      "customer": {
        "username": "customer",
        "password": "customer",
        "email": "kosyrev-2000@mail.ru",
        "role": 1,
        "first_name": "aleks",
        "last_name": "kosyrev",
        "address": "string",
        "geolocation": "37.421925,-122.0841293"
      },
      "is_canceled": False,
      "restaurant": {
         "username": "restaurant",
         "password": "restaurant",
         "email": "rtluats@gmail.com",
         "role": 1,
         "restaurant_name": "rtluats",
         "address": "string",
         "geolocation": "37.421925,-122.0841293"
      },
      "products": [
          {
              "description": "string",
              "weight": "string",
              "price": "string",
              "discount": "string",
              "stocks": [

              ],
              "restaurant": {
                  "username": "restaurant",
                  "password": "restaurant",
                  "email": "rtluats@gmail.com",
                  "role": 1,
                  "restaurant_name": "rtluats",
                  "address": "string",
                  "geolocation": "37.421925,-122.0841293"
              }
          }
      ]
    }
    order_url_create = reverse("order-list")
    client.post(order_url_create, order_json, format="json")
    assert Order.objects.count() == 1
