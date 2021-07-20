from deliver_app.models import Deliver
from deliver_app.serializer import DeliverSerializer
from rest_framework.viewsets import ModelViewSet
from service_app.permissions import CourierPermission


class DeliverView(ModelViewSet):
    serializer_class = DeliverSerializer
    queryset = Deliver.objects.all()
    permission_classes = [CourierPermission,]