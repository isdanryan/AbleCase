from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users, Tasks


class UserCreateForm (UserCreationForm):
    class Meta:
        model = Users
        fields = {
            'email',
            'first_name',
            'last_name',
            # 'role',
            'password1',
            'password2',
        }
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text=(
            "Password must contain at least 8 characters,<br>"
            "including uppercase, lowercase letters,<br>"
            "numbers, and special characters."
        )
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        help_text="Repeat the same password for verification."
    )


class UserUpdateForm (UserCreationForm):
    class Meta:
        model = Users
        fields = {
            'email',
            'first_name',
            'last_name',
            # 'role',
        }
    password1 = forms.CharField(
        label="Password",
        required=False,
        widget=forms.PasswordInput,

        help_text=(
            "Password must contain at least 8 characters,<br>"
            "including uppercase, lowercase letters,<br>"
            "numbers, and special characters."
        )
    )

    password2 = forms.CharField(
        label="Confirm Password",
        required=False,
        widget=forms.PasswordInput,
        help_text="Repeat the same password for verification."
    )


class UserTaskForm (forms.ModelForm):
    class Meta:
        model = Tasks
        fields = {
            'task',
            'due_date',
        }
        widgets = {
            'task': forms.Textarea(attrs={'rows': 3}),
        }


class UserProfileForm (UserChangeForm):
    class Meta:
        model = Users
        fields = {
            'email',
            'first_name',
            'last_name',
        }
    password1 = forms.CharField(
        label="Password",
        required=False,
        widget=forms.PasswordInput,

        help_text=(
            "Password must contain at least 8 characters,<br>"
            "including uppercase, lowercase letters,<br>"
            "numbers, and special characters."
        )
    )

    password2 = forms.CharField(
        label="Confirm Password",
        required=False,
        widget=forms.PasswordInput,
        help_text="Repeat the same password for verification."
    )
