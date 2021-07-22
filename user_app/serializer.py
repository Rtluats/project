from rest_framework import serializers

from user_app.models import Courier, Customer, Restaurant


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = None
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CustomerSerializer(BaseSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'username', 'password', 'email', 'role', 'first_name', 'last_name', 'address', 'geolocation')


class RestaurantSerializer(BaseSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'username', 'password', 'email', 'role', 'restaurant_name', 'address', 'geolocation')


class CourierSerializer(BaseSerializer):
    class Meta:
        model = Courier
        fields = ('id', 'username', 'password', 'email', 'role', 'first_name', 'last_name', 'is_courier_free')