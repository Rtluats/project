from user_app.views import RestaurantView, CustomerView


restaurant_list = RestaurantView.as_view({
    'get': 'list',
    'post': 'create',
})

restaurant_detail = RestaurantView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

customer_list = CustomerView.as_view({
    'get': 'list',
    'post': 'create',
})

customer_detail = CustomerView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})