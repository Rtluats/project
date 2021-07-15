from rest_framework import routers

from complaint_app.views import ComplaintView

complaint_router = routers.SimpleRouter()
complaint_router.register(r'complaint', ComplaintView)


# complaint_list = ComplaintView.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# complaint_detail = ComplaintView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })