from rest_framework import routers

from product_app.views import ProductView, StockView

product_router = routers.SimpleRouter()
product_router.register(r'product', ProductView)
stock_router = routers.SimpleRouter()
stock_router.register(r'stock', StockView)
