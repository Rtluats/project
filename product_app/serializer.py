from rest_framework import serializers

from product_app.models import Product, Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'code', 'description')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'weight', 'price', 'discount', 'stocks', 'restaurant')
