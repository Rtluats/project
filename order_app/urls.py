from rest_framework import routers

from order_app.views import OrderView

order_router = routers.SimpleRouter()
order_router.register(r'order', OrderView)
