from order_app.models import Order
from order_app.serializer import OrderSerializer
from service_app import permissions
from rest_framework.viewsets import ModelViewSet


class OrderView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.IsOwnerOrReadOnlyForOrder,)
