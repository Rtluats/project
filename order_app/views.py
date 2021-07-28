import collections
import decimal

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from basket_app.models import Basket
from order_app.models import Order
from order_app.serializer import OrderSerializer
from service_app import permissions
from user_app.models import Customer


class OrderView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.IsOwnerOrReadOnlyForOrder,)

    def perform_create(self, serializer):
        """this method is necessary in order to divide the products by restaurants and form an order for the customer"""
        restaurant_products = {}
        customer = Customer.objects.get(pk=serializer.data["customer"])
        for product in Basket.objects.get(customer=customer).products.all():
            if product.restaurant not in restaurant_products.keys():
                restaurant_products[product.restaurant] = [product]
            else:
                restaurant_products[product.restaurant].append(product)
        for restaurant in restaurant_products.keys():
            products = restaurant_products[restaurant]
            order = Order.objects.create(customer=customer, restaurant=restaurant, end_price=0)
            order.products.set(products)
            products_count = collections.Counter()
            for product in products:
                products_count[product] += 1
            full_price = decimal.Decimal(0.0)
            discount = decimal.Decimal(0.0)
            for product in products_count.keys():
                if product.stocks is not None:
                    for stock in product.stocks:
                        if stock.code == "1+1" and products_count[product] > 1:
                            discount += product.price - product.price * product.discount
                full_price += (product.price - product.price * product.discount) * products_count[product]
            order.end_price = full_price - discount
            order.save()