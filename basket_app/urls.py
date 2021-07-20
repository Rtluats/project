from rest_framework import routers

from basket_app.views import BasketView

basket_router = routers.SimpleRouter()
basket_router.register(r'basket', BasketView)
