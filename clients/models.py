from django.db import models
from django.utils import timezone


class Clients(models.Model):
    CLIENT_TYPES = {
        "Buisness": "Buisness",
        "Personal": "Personal",
    }
    display_name = models.CharField(max_length=64, blank=False)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    mobile = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=124)
    type = models.CharField(max_length=10, choices=CLIENT_TYPES,
                            blank=False, default="Business")
    building_number = models.CharField(max_length=20)
    street = models.CharField(max_length=64)
    address_2 = models.CharField(max_length=64)
    address_3 = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    post_code = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Clients"
        verbose_name_plural = "Clients"
