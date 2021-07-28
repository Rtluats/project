from rest_framework import serializers

from order_app.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'status', 'end_price', 'customer', 'is_canceled', 'restaurant', 'products')
