from complaint_app.models import Complaint
from complaint_app.serializer import ComplaintSerializer
from service_app.base_classes import BaseView
from service_app.permissions import CustomersPermission


class ComplaintView(BaseView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()
    permission_classes = [CustomersPermission,]