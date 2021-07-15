from rest_framework import routers

from deliver_app.views import DeliverView

deliver_router = routers.SimpleRouter()
deliver_router.register(r'deliver', DeliverView)


# deliver_list = DeliverView.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# deliver_detail = DeliverView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })