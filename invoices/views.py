from django.shortcuts import reverse
from django.views import generic
from .forms import InvoiceForm


class InvoiceCreateView(generic.CreateView):
    template_name = "invoices/invoice_create.html"
    form_class = InvoiceForm

    def get_success_url(self):
        return reverse("cases:case-list")
