from rest_framework import serializers
from deliver_app.models import Deliver
from order_app.serializer import OrderSerializer


class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = ['id', 'order', 'courier', 'is_finished']

    customer = OrderSerializer(many=False)
