from django.shortcuts import reverse, render, redirect
from django.views import generic
from .forms import InvoiceForm
from .models import Invoices
from cases.models import Cases


class InvoiceCreateView(generic.CreateView):
    template_name = "invoices/invoice_create.html"
    form_class = InvoiceForm

    def get_success_url(self):
        return reverse("cases:case-list")


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


class InvoiceListView(generic.ListView):
    template_name = "invoices/invoice_list.html"
    queryset = Invoices.objects.all()
    context_object_name = "invoices"


class InvoiceCaseView(generic.ListView):
    template_name = "invoices/invoice_select_case.html"
    queryset = Cases.objects.all()
    context_object_name = "cases"


def SelectCase(request):
    case_form = SelectCaseForm()
    invoice_form = InvoiceForm()
    if request.method == "POST":
        print('Reciving a post')
    context = {
        "case_form": case_form,
        "invoice_form": invoice_form
    }
    return render(request, "invoices/invoice_create.html", context)
