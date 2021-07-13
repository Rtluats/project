from product_app.models import Stock, Product
from product_app.serializer import StockSerializer, ProductSerializer
from service_app.permissions import IsOwnerOrReadOnly
from service_app.base_classes import BaseView


class StockView(BaseView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [IsOwnerOrReadOnly,]


class ProductView(BaseView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsOwnerOrReadOnly,]
