from rest_framework import viewsets
from product_app.models import Stock, Product
from product_app.serializer import StockSerializer, ProductSerializer
from service_app.permissions import IsOwnerOrReadOnly


class StockView(viewsets.mixins.ListModelMixin,
                viewsets.mixins.RetrieveModelMixin,
                viewsets.mixins.CreateModelMixin,
                viewsets.mixins.UpdateModelMixin,
                viewsets.mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [IsOwnerOrReadOnly,]


class ProductView(viewsets.mixins.ListModelMixin,
                  viewsets.mixins.RetrieveModelMixin,
                  viewsets.mixins.CreateModelMixin,
                  viewsets.mixins.UpdateModelMixin,
                  viewsets.mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsOwnerOrReadOnly,]
