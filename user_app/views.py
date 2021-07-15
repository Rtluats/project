from rest_framework.permissions import AllowAny

from service_app.base_classes import BaseView
from service_app.permissions import IsOwnerOrReadOnly
from user_app.models import Courier, Customer, Restaurant
from user_app.serializer import (CourierSerializer, CustomerSerializer,
                                 RestaurantSerializer)


class RestaurantView(BaseView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny(),]
        else:
            return [IsOwnerOrReadOnly(),]


class CustomerView(BaseView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny(),]
        else:
            return [IsOwnerOrReadOnly(),]


class CourierView(BaseView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny(),]
        else:
            return [IsOwnerOrReadOnly(),]