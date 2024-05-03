from django.db import models
from django.utils import timezone


class Clients(models.Model):
    CLIENT_TYPES = {
        "Buisness": "Buisness",
        "Personal": "Personal",
    }
    display_name = models.CharField(max_length=64, blank=False)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    middle_name = models.CharField(max_length=64, blank=True)
    mobile = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(max_length=124, blank=True)
    type = models.CharField(max_length=10, choices=CLIENT_TYPES,
                            blank=False, default="Business")
    building_number = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=64, blank=True)
    address_2 = models.CharField(max_length=64, blank=True)
    address_3 = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    post_code = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Clients"
        verbose_name_plural = "Clients"
