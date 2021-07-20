from rest_framework import serializers

from complaint_app.models import Complaint
from order_app.serializer import OrderSerializer
from user_app.serializer import CourierSerializer


class ComplaintSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=False)
    courier = CourierSerializer(many=False)

    class Meta:
        model = Complaint
        fields = ('id', 'order', 'courier', 'message', 'datetime_created')
