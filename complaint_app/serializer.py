from rest_framework import serializers

from complaint_app.models import Complaint
from deliver_app.serializer import DeliverSerializer


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['id', 'deliver', 'message', 'datetime_created']

    deliver = DeliverSerializer(many=False)
