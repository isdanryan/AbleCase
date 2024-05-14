from django.db import models
from django.utils import timezone


class InvoiceCode(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    short_code = models.CharField(max_length=2, blank=False, null=False)

    def __str__(self):
        return f"{self.short_code} - {self.name}"


class Invoices(models.Model):
    INVOICE_TERM = {
        "On Reciept": "On Reciept",
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
    invoice_number = models.CharField(max_length=6, blank=False, null=False)
    date = models.DateField(default=timezone.now)
    term = models.CharField(max_length=64, choices=INVOICE_TERM, blank=False,
                            null=False, default="On Reciept")
    date_due = models.DateField(default=timezone.now)
    amount = models.FloatField()
    vat = models.FloatField()
    total_due = models.FloatField()
    case = models.ForeignKey("cases.Cases", on_delete=models.CASCADE)
    client = models.ForeignKey("clients.Clients", on_delete=models.PROTECT)
    status = models.CharField(max_length=64, choices=INVOICE_STATUS,
                              blank=False, null=False, default="Not Sent")
