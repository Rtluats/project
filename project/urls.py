"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# from user_app.urls import (courier_detail, courier_list, customer_detail,
#                            customer_list, restaurant_detail, restaurant_list)
# from complaint_app.urls import complaint_detail, complaint_list
# from deliver_app.urls import deliver_detail, deliver_list
from basket_app.urls import basket_router
from complaint_app.urls import complaint_router
from deliver_app.urls import deliver_router
from order_app.urls import order_router
from product_app.urls import product_router, stock_router
# from basket_app.urls import basket_detail, basket_list
# from order_app.urls import order_detail, order_list
# from product_app.urls import product_detail, product_list
from project.yasg import swagger
from user_app.urls import courier_router, customer_router, restaurant_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('api/v1/restaurants/', restaurant_list, name='restaurant-list'),
    # path('api/v1/restaurant/<int:pk>/', restaurant_detail, name='restaurant-detail'),
    # path('api/v1/customers/', customer_list, name='customer-list'),
    # path('api/v1/customer/<int:pk>/', customer_detail, name=' customer_detail'),
    # path('api/v1/products/', product_list, name='product-list'),
    # path('api/v1/product/<int:pk>/', product_detail, name='product-detail'),
    # path('api/v1/orders/', order_list, name='order-list'),
    # path('api/v1/order/<int:pk>/', order_detail, name='order-detail'),
    # path('api/v1/baskets/', basket_list, name='basket_list'),
    # path('api/v1/basket/<int:pk>/', basket_detail, name='basket-detail'),
    # path('api/v1/couriers/', courier_list, name='courier_list'),
    # path('api/v1/courier/<int:pk>/', courier_detail, name='courier-detail'),
    # path('api/v1/complaint/', complaint_list, name=' complaint_list'),
    # path('api/v1/complaint/<int:pk>/', complaint_detail, name='complaint-detail'),
    # path('api/v1/deliver/', deliver_list, name='deliver_list'),
    # path('api/v1/deliver/<int:pk>/', deliver_detail, name='deliver-detail'),
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