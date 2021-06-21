from basket_app.views import BasketView


basket_list = BasketView.as_view({
    'get': 'list',
    'post': 'create',
})

basket_detail = BasketView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})