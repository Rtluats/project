from order_app.models import Order
from order_app.serializer import OrderSerializer
from service_app import permissions
from service_app.base_classes import BaseView


class OrderView(BaseView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.IsOwnerOrReadOnlyForOrder,)


