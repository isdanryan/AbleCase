from django import forms
from .models import Clients


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = (
            'display_name',
            'first_name',
            'last_name',
            'middle_name',
            'mobile',
            'phone',
            'email',
            'type',
            'building_number',
            'street',
            'address_2',
            'address_3',
            'city',
            'post_code',
            'notes',
        )
