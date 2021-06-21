from rest_framework import viewsets
from user_app.models import Restaurant, Customer
from user_app.serializer import RestaurantSerializer, CustomerSerializer


class RestaurantView(viewsets.mixins.ListModelMixin,
                     viewsets.mixins.RetrieveModelMixin,
                     viewsets.mixins.CreateModelMixin,
                     viewsets.mixins.UpdateModelMixin,
                     viewsets.mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class CustomerView(viewsets.mixins.ListModelMixin,
                   viewsets.mixins.RetrieveModelMixin,
                   viewsets.mixins.CreateModelMixin,
                   viewsets.mixins.UpdateModelMixin,
                   viewsets.mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
