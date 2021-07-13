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
from django.urls import path, include
from user_app.urls import (
    restaurant_list, restaurant_detail, customer_list, customer_detail, courier_list, courier_detail
)
from product_app.urls import product_list, product_detail
from order_app.urls import order_list, order_detail
from basket_app.urls import basket_list, basket_detail
from project.yasg import swagger


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/restaurants/', restaurant_list, name='restaurant-list'),
    path('api/v1/restaurant/<int:pk>/', restaurant_detail, name='restaurant-detail'),
    path('api/v1/customers/', customer_list, name='customer-list'),
    path('api/v1/customer/<int:pk>/', customer_detail, name=' customer_detail'),
    path('api/v1/products/', product_list, name='product-list'),
    path('api/v1/product/<int:pk>/', product_detail, name='product-detail'),
    path('api/v1/orders/', order_list, name='order-list'),
    path('api/v1/order/<int:pk>/', order_detail, name='order-detail'),
    path('api/v1/baskets/', basket_list, name='basket_list'),
    path('api/v1/basket/<int:pk>/', basket_detail, name='basket-detail'),
    path('api/v1/couriers/', courier_list, name='courier_list'),
    path('api/v1/courier/<int:pk>/', courier_detail, name='courier-detail'),
    swagger,
]