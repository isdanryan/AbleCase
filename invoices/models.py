from django.db import models


class InvoiceCode(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    short_code = models.CharField(max_length=2, blank=False, null=False)

    def __str__(self):
        return f"{self.short_code} - {self.name}"
