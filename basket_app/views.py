from rest_framework import viewsets
from basket_app.models import Basket
from basket_app.serializer import BasketSerializer
from service_app import permissions


class BasketView(viewsets.mixins.ListModelMixin,
                 viewsets.mixins.RetrieveModelMixin,
                 viewsets.mixins.CreateModelMixin,
                 viewsets.mixins.UpdateModelMixin,
                 viewsets.mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
    permission_classes = (permissions.IsOwnerOrReadOnly,)