from basket_app.models import Basket
from basket_app.serializer import BasketSerializer
from service_app import permissions
from service_app.base_classes import BaseView


class BasketView(BaseView):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
    permission_classes = (permissions.IsOwnerOrReadOnly,)