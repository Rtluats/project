from rest_framework import routers

from product_app.views import ProductView, StockView

product_router = routers.SimpleRouter()
product_router.register(r'product', ProductView)
stock_router = routers.SimpleRouter()
stock_router.register(r'stock', StockView)

# product_list = ProductView.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# product_detail = ProductView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# stock_list = StockView.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# stock_detail = StockView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })