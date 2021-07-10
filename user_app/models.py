from django.db import models
from django.contrib.auth.models import AbstractUser
from django_google_maps import fields as map_fields
# Create your models here.


class User(AbstractUser):
    class Role(models.IntegerChoices):
        CUSTOMER = 1, "Customer"
        RESTAURANT = 2, "Restaurant"
        COURIER = 3, "Courier"
    role = models.PositiveSmallIntegerField(choices=Role.choices, default=Role.CUSTOMER)
    restaurant_name = models.CharField(max_length=300, blank=True)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    is_courier_free = models.BooleanField(default=False)

    @property
    def owner(self):
        return self


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


class CourierManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.COURIER)


class Courier(User):
    objects = CourierManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Role.COURIER
            self.is_courier_free = True
        return super().save(*args, **kwargs)