from django import forms
from clients.models import Clients
from users.models import Users
from django.contrib.auth.forms import UserCreationForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = (
            'display_name',
            'mobile',
            'phone',
            'email',
            'building_number',
            'street',
            'address_2',
            'address_3',
            'city',
            'post_code',
            'client_reference',
        )


class ClientLoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class PortalSignupForm(UserCreationForm):
    client_reference = forms.CharField(max_length=16)

    class Meta:
        model = Users
        fields = ('email', 'password1', 'password2', 'client_reference')

    def clean_reference_number(self):
        client_reference = self.cleaned_data['client_reference']
        # Check if the reference number exists in the Client model
        if not Clients.objects.filter(client_reference=client_reference).exists():
            raise forms.ValidationError("Invalid reference number.")
        else:
            print("Found client profile")
        return client_reference
