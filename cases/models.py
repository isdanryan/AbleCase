from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from invoices.models import InvoiceCode


class Cases(models.Model):
    CASE_STATUS = {
        "Open": "Open",
        "Closed": "Closed",
    }
    case_number = models.IntegerField(blank=False)
    case_name = models.CharField(max_length=64, blank=True)
    type = models.ForeignKey("CaseTypes", on_delete=models.PROTECT)
    invoice_code = models.ForeignKey("invoices.InvoiceCode",
                                     on_delete=models.SET_NULL, null=True)
    address = models.TextField()
    phone = PhoneNumberField(blank=False)
    review_date = models.DateTimeField(default=timezone.now)
    assigned = models.CharField(max_length=64, blank=True)
    status = models.CharField(max_length=10, choices=CASE_STATUS, blank=False,
                              default="Open")
    notes = models.TextField(blank=True)
    client = models.ForeignKey("clients.Clients",
                               on_delete=models.SET_NULL,
                               null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cases"
        verbose_name_plural = "Cases"

    def __str__(self):
        return self.case_name


class CaseTypes(models.Model):
    type = models.CharField(max_length=64, blank=False, null=False)

    class Meta:
        verbose_name = "Case Types"
        verbose_name_plural = "Case Types"

    def __str__(self):
        return self.type
