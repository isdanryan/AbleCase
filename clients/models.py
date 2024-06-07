from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        BaseUserManager)
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Clients(models.Model):
    CLIENT_TYPES = {
        "Buisness": "Buisness",
        "Individual": "Individual",
    }
    CLIENT_STATUS = {
        "Active": "Active",
        "Inactive": "Inactive",
    }
    display_name = models.CharField(max_length=64, blank=False)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    middle_name = models.CharField(max_length=64, blank=True)
    mobile = PhoneNumberField(blank=True, null=True)
    phone = PhoneNumberField(blank=False)
    email = models.EmailField(max_length=124, blank=True)
    type = models.CharField(max_length=10, choices=CLIENT_TYPES,
                            blank=False, default="Business")
    building_number = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=64, blank=True)
    address_2 = models.CharField(max_length=64, blank=True)
    address_3 = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    post_code = models.CharField(max_length=64, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=CLIENT_STATUS,
                              blank=False, null=False, default="Active")
    has_portal_access = models.BooleanField(default=False)
    portal_account = models.OneToOneField("users.Users", null=True,
                                          on_delete=models.PROTECT)
    client_reference = models.CharField(max_length=16, unique=True,
                                        blank=False, null=False)

    class Meta:
        verbose_name = "Clients"
        verbose_name_plural = "Clients"

        permissions = [
            ("can_view_clients", "View Clients"),
            ("can_edit_clients", "Edit Clients"),
        ]

    def __str__(self):
        return self.display_name
