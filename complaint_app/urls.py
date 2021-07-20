from rest_framework import routers

from complaint_app.views import ComplaintView

complaint_router = routers.SimpleRouter()
complaint_router.register(r'complaint', ComplaintView)
