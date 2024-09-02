from django.db import models


class Payment(models.Model):
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    invoice = models.ForeignKey('invoices.Invoices', on_delete=models.CASCADE)
    amount_payed = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_charge_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment {self.stripe_charge_id} \
            for {self.invoice.invoice_number}'
