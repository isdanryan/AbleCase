from django import forms
from .models import Cases, Communications


class CaseForm(forms.ModelForm):
    class Meta:
        model = Cases
        fields = (
            'case_number',
            'case_name',
            'type',
            'invoice_code',
            'address',
            'phone',
            'review_date',
            'assigned',
            'status',
            'notes',
            'client',
        )


class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communications
        fields = (
            'details',
            'date',
        )
