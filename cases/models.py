from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


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
    address = models.CharField(max_length=240, blank=True, null=True)
    phone = PhoneNumberField(blank=False)
    review_date = models.DateField(default=timezone.now)
    assigned = models.CharField(max_length=64, blank=True)
    status = models.CharField(max_length=10, choices=CASE_STATUS, blank=False,
                              default="Open")
    notes = models.TextField(blank=True)
    client = models.ForeignKey("clients.Clients",
                               on_delete=models.PROTECT,
                               null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cases"
        verbose_name_plural = "Cases"
        
        permissions = [
            ("can_view_cases", "View Case"),
            ("can_edit_cases", "Edit Case"),
        ]

    def __str__(self):
        return self.case_name


class CaseTypes(models.Model):
    type = models.CharField(max_length=64, blank=False, null=False)

    class Meta:
        verbose_name = "Case Types"
        verbose_name_plural = "Case Types"

    def __str__(self):
        return self.type


class Communications(models.Model):
    details = models.TextField(blank=False)
    date = models.DateTimeField(default=timezone.now)
    case = models.ForeignKey("Cases", on_delete=models.CASCADE,
                             blank=False, null=False)

    def __str__(self):
        return f"{self.case} - {self.date}"
