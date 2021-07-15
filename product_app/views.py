from product_app.models import Product, Stock
from product_app.serializer import ProductSerializer, StockSerializer
from service_app.base_classes import BaseView
from service_app.permissions import IsOwnerOrReadOnly, RestaurantPermission


class StockView(BaseView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [IsOwnerOrReadOnly, RestaurantPermission]


class ProductView(BaseView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsOwnerOrReadOnly, RestaurantPermission]
