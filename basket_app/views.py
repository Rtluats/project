from basket_app.models import Basket
from basket_app.serializer import BasketSerializer
from service_app import permissions
from rest_framework.viewsets import ModelViewSet


class BasketView(ModelViewSet):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
    permission_classes = (permissions.IsOwnerOrReadOnly,)