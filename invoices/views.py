from django.shortcuts import render, reverse
from django.views import generic
from .models import Invoices
from .forms import InvoiceForm


class InvoiceCreateView(generic.CreateView):
    template_name = "invoices/invoice_create.html"
    form_class = InvoiceForm

    def get_success_url(self):
        return reverse("cases:case-list")
