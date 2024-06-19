from typing import Any
#from django.db.models.query import QuerySet
from django.shortcuts import reverse, render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import InvoiceForm
from .models import Invoices
from cases.models import Cases
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
#from django.contrib.staticfiles import finders
from django.shortcuts import get_object_or_404
from ablecase.mixins import RoleRequiredMixin
from ablecase.decorators import role_required


# Create a new invoice from the selected case
@login_required
@role_required("Staff")
def CreateInvoice(request, pk):
    case = get_object_or_404(Cases, id=pk)
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoices:invoice-list')
    else:
        # Get the last invoice number and increase by 1
        last_invoice_number = Invoices.objects.values_list('invoice_number',
                                                           flat=True).last()
        if last_invoice_number is not None:
            next_invoice_number = last_invoice_number + 1
        else:
            # If it's a new invoice set to blank
            next_invoice_number = ''
        # Get and set the data from the required fields
        set_data = {
            'invoice_number': next_invoice_number,
            'client': case.client,
            'case_name': case.case_name,
            'case_address': case.address,
            'case_type': case.type,
            'invoice_code': case.invoice_code,
            'case': case,
        }
        # Pass the data to the form for rendering
        form = InvoiceForm(initial=set_data)  
    return render(request, 'invoices/invoice_create.html',
                  {'form': form, 'case': case})


# View to update the selected invoice details
class InvoiceUpdateView(LoginRequiredMixin, RoleRequiredMixin, generic.UpdateView):
    template_name = "invoices/invoice_update.html"
    form_class = InvoiceForm
    queryset = Invoices.objects.all()
    context_object_name = "invoice"
    # Only allow access if the user has the staff role
    required_role = "Staff"

    def get_success_url(self):
        return reverse("invoices:invoice-list")


class InvoiceListView(LoginRequiredMixin, RoleRequiredMixin, generic.ListView):
    template_name = "invoices/invoice_list.html"
    queryset = Invoices.objects.all()
    context_object_name = "invoices"
    # Only allow access if the user has the staff role
    required_role = "Staff"

    # Set out the search function to search invoices by invoice number
    def get_queryset(self):
        queryset = Invoices.objects.all()
        search_query = self.request.GET.get('search', '')
        filter = self.request.GET.get('filter')

        # Check for filter
        if filter == 'notsent':
            queryset = queryset.filter(status='Not Sent')
        elif filter == 'sent':
            queryset = queryset.filter(status='Sent')
        elif filter == 'paid':
            queryset = queryset.filter(status='Paid')

        if search_query:
            queryset = queryset.filter(invoice_number__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['filter'] = self.request.GET.get('filter')
        return context


# Create view to allow user to select a case to create an invoice for
class InvoiceCaseView(LoginRequiredMixin, RoleRequiredMixin, generic.ListView):
    template_name = "invoices/invoice_select_case.html"
    queryset = Cases.objects.all()
    context_object_name = "cases"
    # Only allow access if the user has the staff role
    required_role = "Staff"

    # Set out the search function to search invoices by case number
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


# Setup the file paths for the pdf create function to use
def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths
    so xhtml2pdf can access those resources
    """
    # Handle external URLs separately
    if uri.startswith("http://") or uri.startswith("https://"):
        return uri

    # Set path for static
    sUrl = settings.STATIC_URL        
    sRoot = settings.STATICFILES_DIRS[0] 

    if uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        raise RuntimeError('media URI must start with %s' % sUrl)

    # make sure that file exists
    if not os.path.isfile(path):
        raise RuntimeError('File not found: %s' % path)
    return path


# Function to create the pdf from the selected invoice
def pdf_view(request, pk):
    # Get all the data
    invoice = get_object_or_404(Invoices, id=pk)
    template_path = 'invoices/invoice_template.html'
    context = {'invoice': invoice}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.invoice_number}.pdf"'

    # Find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # Create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)

    # If error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
