from rest_framework import routers

from user_app.views import CourierView, CustomerView, RestaurantView

courier_router = routers.SimpleRouter()
courier_router.register(r'courier', CourierView)
customer_router = routers.SimpleRouter()
customer_router.register(r'customer', CustomerView)
restaurant_router = routers.SimpleRouter()
restaurant_router.register(r'restaurant', RestaurantView)
