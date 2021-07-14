from rest_framework import serializers
from order_app.models import Order
from user_app.serializer import CustomerSerializer, RestaurantSerializer
from basket_app.serializer import BasketSerializer
from product_app.serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'basket', 'end_price', 'customer', 'is_canceled', 'restaurant', 'products']

    customer = CustomerSerializer(many=False)
    basket = BasketSerializer(many=False)
    restaurant = RestaurantSerializer(many=False)
    products = ProductSerializer(many=True)