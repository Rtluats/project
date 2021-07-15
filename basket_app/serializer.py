from rest_framework import serializers

from basket_app.models import Basket
from product_app.serializer import ProductSerializer
from user_app.serializer import CustomerSerializer


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['id', 'customer', 'products']

    customer = CustomerSerializer(many=False)
    products = ProductSerializer(many=True)
