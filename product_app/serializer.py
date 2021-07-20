from rest_framework import serializers

from product_app.models import Product, Stock
from user_app.serializer import RestaurantSerializer


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'code', 'description')


class ProductSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True)
    restaurant = RestaurantSerializer(many=False)

    class Meta:
        model = Product
        fields = ('id', 'description', 'weight', 'price', 'discount', 'stocks', 'restaurant')
