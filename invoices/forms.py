from django import forms
from .models import Invoices
from cases.models import Cases


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoices
        fields = (
            'invoice_number',
            'date',
            'client',
            'term',
            'date_due',
            'case',
            'amount',
            'vat',
            'total_due',
            'status',
            'case_name',
            'case_address',
            'case_type',
            'invoice_code',
            'notes',
        )


class SearchForm(forms.ModelForm):
    model = Cases
    fields = (
        'case_number',
    )