from django.db import models
from django.utils import timezone


class InvoiceCode(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    short_code = models.CharField(max_length=2, blank=False, null=False)

    def __str__(self):
        return f"{self.short_code} - {self.name}"


class Invoices(models.Model):
    INVOICE_TERM = {
        "On Receipt": "On Receipt",
        "7 Days": "7 days",
        "14 Days": "14 days",
        "30 Days": "30 days",
        "Custom": "Custom",
    }
    INVOICE_STATUS = {
        "Paid": "Paid",
        "Sent": "Sent",
        "Not Sent": "Not Sent",
    }
    VAT = {
        "ZERO": "ZERO",
        "10%": "10%",
        "15%": "15%",
        "20%": "20%",
    }
    invoice_number = models.IntegerField(blank=False, null=False,
                                         verbose_name="Invoice No")
    date = models.DateField(default=timezone.now)
    term = models.CharField(max_length=64, choices=INVOICE_TERM, blank=False,
                            null=False, default="On Reciept")
    date_due = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=19, decimal_places=2,
                                 default="0.00")
    vat = models.CharField(max_length=10, choices=VAT,
                           blank=False, null=False, default="20%")
    total_due = models.DecimalField(max_digits=19, decimal_places=2,
                                    default="0.00")
    case = models.ForeignKey("cases.Cases", on_delete=models.CASCADE)
    case_address = models.CharField(max_length=256, blank=True, null=True)
    case_type = models.CharField(max_length=64, blank=True, null=True)
    case_name = models.CharField(max_length=64, blank=True, null=True)
    invoice_code = models.CharField(max_length=20, blank=True, null=True)
    client = models.ForeignKey("clients.Clients", on_delete=models.PROTECT)
    status = models.CharField(max_length=64, choices=INVOICE_STATUS,
                              blank=False, null=False, default="Not Sent")
    notes = models.TextField()
