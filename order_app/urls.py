from rest_framework import routers

from order_app.views import OrderView

order_router = routers.SimpleRouter()
order_router.register(r'order', OrderView)

# order_list = OrderView.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# order_detail = OrderView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })