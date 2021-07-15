from rest_framework import routers

from basket_app.views import BasketView

basket_router = routers.SimpleRouter()
basket_router.register(r'basket', BasketView)

# basket_list = BasketView.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# basket_detail = BasketView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })