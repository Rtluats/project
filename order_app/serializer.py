from rest_framework import serializers
from order_app.models import Order
from user_app.serializer import CustomerSerializer
from basket_app.serializer import BasketSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'basket', 'end_price', 'customer', 'is_finished']

    customer = CustomerSerializer(many=False)
    basket = BasketSerializer(many=False)
