from product_app.models import Product, Stock
from product_app.serializer import ProductSerializer, StockSerializer
from rest_framework.viewsets import ModelViewSet
from service_app.permissions import IsOwnerOrReadOnly, RestaurantPermission


class StockView(ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [IsOwnerOrReadOnly, RestaurantPermission]


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsOwnerOrReadOnly, RestaurantPermission]
