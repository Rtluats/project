from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from service_app.permissions import IsOwnerOrReadOnly
from user_app.models import Courier, Customer, Restaurant
from user_app.serializer import (CourierSerializer, CustomerSerializer,
                                 RestaurantSerializer)


class RestaurantView(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny(),]
        else:
            return [IsOwnerOrReadOnly(),]


class CustomerView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny(),]
        return [IsOwnerOrReadOnly(),]


class CourierView(ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny(),]
        return [IsOwnerOrReadOnly(),]
