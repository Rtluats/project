import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from complaint_app.models import Complaint
from order_app.models import Order
from service_app.email_tasks import common
from user_app.models import Courier


class Deliver(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name="courier", null=True)
    is_finished = models.BooleanField(default=False)


@receiver(signal=post_save, sender=Deliver)
def deliver_post_save(sender, instance: Deliver, *args, **kwargs):
    if instance.is_finished is True:
        complaint = Complaint()
        complaint.courier = instance.courier
        complaint.order = instance.order
        complaint.datetime_created = datetime.datetime.now()
        complaint.save()
        url_on_complaint = reverse("order-detail", kwargs={'pk': complaint.id})
        url_on_order = reverse("order-detail", kwargs={'pk': instance.order.id})
        common.delay(url_on_order, instance.order.customer.email, "Заказ доставлен! Жалоба ( ссылка действительна 5 "
                                                                  "минут) -> " + url_on_complaint)