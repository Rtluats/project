from rest_framework import serializers

from deliver_app.models import Deliver
from order_app.serializer import OrderSerializer
from user_app.serializer import CourierSerializer


class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = ['id', 'order', 'courier', 'is_finished']

    order = OrderSerializer(many=False)
    courier = CourierSerializer(many=False)
