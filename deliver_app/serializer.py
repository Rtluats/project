from rest_framework import serializers

from deliver_app.models import Deliver


class DeliverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deliver
        fields = ('id', 'order', 'courier', 'is_finished')
