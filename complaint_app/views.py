from complaint_app.models import Complaint
from complaint_app.serializer import ComplaintSerializer
from rest_framework.viewsets import ModelViewSet
from service_app.permissions import CustomersPermission


class ComplaintView(ModelViewSet):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()
    permission_classes = [CustomersPermission,]