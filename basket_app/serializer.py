from rest_framework import serializers

from basket_app.models import Basket


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ('id', 'customer', 'products')
