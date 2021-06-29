from rest_framework import viewsets
from user_app.models import Restaurant, Customer
from user_app.serializer import RestaurantSerializer, CustomerSerializer
from rest_framework.permissions import AllowAny
from service_app.permissions import IsOwnerOrReadOnly


class RestaurantView(viewsets.mixins.ListModelMixin,
                     viewsets.mixins.RetrieveModelMixin,
                     viewsets.mixins.CreateModelMixin,
                     viewsets.mixins.UpdateModelMixin,
                     viewsets.mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny(),]
        else:
            return [IsOwnerOrReadOnly(),]


class CustomerView(viewsets.mixins.ListModelMixin,
                   viewsets.mixins.RetrieveModelMixin,
                   viewsets.mixins.CreateModelMixin,
                   viewsets.mixins.UpdateModelMixin,
                   viewsets.mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny(),]
        else:
            return [IsOwnerOrReadOnly(),]