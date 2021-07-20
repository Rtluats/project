from rest_framework import routers

from deliver_app.views import DeliverView

deliver_router = routers.SimpleRouter()
deliver_router.register(r'deliver', DeliverView)
