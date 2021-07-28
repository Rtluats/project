from django.contrib import admin
from django.urls import include, path

from basket_app.urls import basket_router
from complaint_app.urls import complaint_router
from deliver_app.urls import deliver_router
from order_app.urls import order_router
from product_app.urls import product_router, stock_router
from project.yasg import swagger
from user_app.urls import courier_router, customer_router, restaurant_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/', include(basket_router.urls)),
    path('api/v1/', include(complaint_router.urls)),
    path('api/v1/', include(deliver_router.urls)),
    path('api/v1/', include(order_router.urls)),
    path('api/v1/', include(product_router.urls)),
    path('api/v1/', include(stock_router.urls)),
    path('api/v1/', include(customer_router.urls)),
    path('api/v1/', include(courier_router.urls)),
    path('api/v1/', include(restaurant_router.urls)),
    swagger,
]
