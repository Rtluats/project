from django.db import models
from django.contrib.auth.models import AbstractUser
from django_google_maps import fields as map_fields
# Create your models here.


class User(AbstractUser):
    class Role(models.IntegerChoices):
        CUSTOMER = 1, "Customer"
        RESTAURANT = 2, "Restaurant"
    role = models.PositiveSmallIntegerField(choices=Role.choices, default=Role.CUSTOMER)
    restaurant_name = models.CharField(max_length=300, blank=True)
    geolocation = map_fields.GeoLocationField(max_length=100)


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.CUSTOMER)


class Customer(User):
    objects = CustomerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Role.CUSTOMER
        return super().save(*args, *kwargs)


class RestaurantManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.RESTAURANT)


class Restaurant(User):
    objects = RestaurantManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Role.RESTAURANT
        return super().save(*args, **kwargs)