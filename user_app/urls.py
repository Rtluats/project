from user_app.views import CourierView, CustomerView, RestaurantView

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

courier_list = CourierView.as_view({
    'get': 'list',
    'post': 'create',
})

courier_detail = CourierView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})