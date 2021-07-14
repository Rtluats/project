from service_app.base_classes import BaseView
from complaint_app.serializer import ComplaintSerializer
from complaint_app.models import Complaint


class ComplaintView(BaseView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()