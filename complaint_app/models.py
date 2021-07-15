import datetime

from django.core.exceptions import PermissionDenied
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from order_app.models import Order
from user_app.models import Courier


class Complaint(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    message = models.TextField(max_length=512)
    datetime_created = models.DateTimeField()


@receiver(signal=pre_save, sender=Complaint)
def order_pre_save(sender, instance: Complaint, *args, **kwargs):
    if instance.id is not None :
        delta = datetime.datetime.now() - instance.datetime_created
        if delta.total_seconds() > datetime.timedelta(minutes=5).total_seconds():
            raise PermissionDenied
