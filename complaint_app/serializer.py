from rest_framework import serializers

from complaint_app.models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = ('id', 'order', 'courier', 'message', 'datetime_created')
