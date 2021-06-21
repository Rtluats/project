from rest_framework import viewsets
from order_app.models import Order
from order_app.serializer import OrderSerializer


class OrderView(viewsets.mixins.ListModelMixin,
                viewsets.mixins.RetrieveModelMixin,
                viewsets.mixins.CreateModelMixin,
                viewsets.mixins.UpdateModelMixin,
                viewsets.mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

