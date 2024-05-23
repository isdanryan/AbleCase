from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import reverse, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import InvoiceForm
from .models import Invoices
from cases.models import Cases


class InvoiceCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "invoices/invoice_create.html"
    form_class = InvoiceForm

    def get_success_url(self):
        return reverse("cases:case-list")


@login_required
def CreateInvoice(request, pk):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoices/invoice_list.html')
    else:
        # Set the instance to the selected case,
        case = Cases.objects.get(id=pk)
        case_number = case.case_number
        # Get the last invoice number and increase by 1
        last_invoice_number = Invoices.objects.values_list('invoice_number',
                                                           flat=True).last()
        if last_invoice_number is not None:
            next_invoice_number = last_invoice_number + 1
        else:
            next_invoice_number = ''
        # and get all required fields from the instance
        set_data = {
            'invoice_number': next_invoice_number,
            'client': case.client,
            'case_name': case.case_name,
            'case_address': case.address,
            'case_type': case.type,
            'invoice_code': case.invoice_code,
            'case': case,
        }
        form = InvoiceForm(initial=set_data)  # Pass case data to the form
    return render(request, 'invoices/invoice_create.html',
                  {'form': form, 'case_number': case_number})


class InvoiceListView(LoginRequiredMixin, generic.ListView):
    template_name = "invoices/invoice_list.html"
    queryset = Invoices.objects.all()
    context_object_name = "invoices"


class InvoiceCaseView(LoginRequiredMixin, generic.ListView):
    template_name = "invoices/invoice_select_case.html"
    queryset = Cases.objects.all()
    context_object_name = "cases"

    def get_queryset(self):
        queryset = Cases.objects.all()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(case_number__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context
