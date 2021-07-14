from service_app.base_classes import BaseView
from deliver_app.serializer import DeliverSerializer
from deliver_app.models import Deliver


class DeliverView(BaseView):
    serializer_class = DeliverSerializer
    queryset = Deliver.objects.all()