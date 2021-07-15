from order_app.views import OrderView

order_list = OrderView.as_view({
    'get': 'list',
    'post': 'create',
})

order_detail = OrderView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})