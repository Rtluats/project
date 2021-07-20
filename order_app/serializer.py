from rest_framework import serializers

from basket_app.serializer import BasketSerializer
from order_app.models import Order
from product_app.serializer import ProductSerializer
from user_app.serializer import CustomerSerializer, RestaurantSerializer


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False)
    basket = BasketSerializer(many=False)
    restaurant = RestaurantSerializer(many=False)
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'status', 'basket', 'end_price', 'customer', 'is_canceled', 'restaurant', 'products')
