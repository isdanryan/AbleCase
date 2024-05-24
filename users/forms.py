from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users


class UserCreateForm (UserCreationForm):
    class Meta:
        model = Users
        fields = {
            'email',
            'first_name',
            'last_name',
            'role',
            'password1',
            'password2',
        }