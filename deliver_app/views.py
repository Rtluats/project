from deliver_app.models import Deliver
from deliver_app.serializer import DeliverSerializer
from service_app.base_classes import BaseView
from service_app.permissions import CourierPermission


class DeliverView(BaseView):
    serializer_class = DeliverSerializer
    queryset = Deliver.objects.all()
    permission_classes = [CourierPermission,]