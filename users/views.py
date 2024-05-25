from typing import Any
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission
from django.db.models import Q
from .models import Users
from .forms import UserCreateForm, UserUpdateForm
from django.views import generic
from django.contrib import messages


class UserCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "users/user_create.html"
    form_class = UserCreateForm
    model = Users

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.data = form.data.copy()
        if self.request.method == 'POST':
            email = self.request.POST.get('email')
            if email:
                form.data['user_name'] = email
        return form

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_name = form.cleaned_data["email"]
        user.set_password(form.cleaned_data["password1"])
        user.save()

        # Check for permissions and if true, assign the permission
        if self.request.POST.get('view_cases'):
            permission = Permission.objects.get(codename='can_view_cases')
            user.user_permissions.add(permission)

        if self.request.POST.get('edit_cases'):
            permission = Permission.objects.get(codename='can_edit_cases')
            user.user_permissions.add(permission)

        if self.request.POST.get('view_clients'):
            permission = Permission.objects.get(codename='can_view_clients')
            user.user_permissions.add(permission)

        if self.request.POST.get('edit_clients'):
            permission = Permission.objects.get(codename='can_edit_clients')
            user.user_permissions.add(permission)

        if self.request.POST.get('manage_invoices'):
            permission = Permission.objects.get(codename='manage_invoices')
            user.user_permissions.add(permission)

        if self.request.POST.get('manage_users'):
            permission = Permission.objects.get(codename='manage_users')
            user.user_permissions.add(permission)

        if self.request.POST.get('allow_signin'):
            user.is_active = True

        return redirect(self.get_success_url())

    def form_invalid(self, form):
        print("Form is invalid. Errors:")
        for field, errors in form.errors.items():
            for error in errors:
                print(f"{field}: {error}")
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("users:user-list")


class UserListView(LoginRequiredMixin, generic.ListView):
    template_name = "users/user_list.html"
    context_object_name = "users"

    def get_queryset(self):
        queryset = Users.objects.filter(Q(role='Staff') | Q(role='Admin')).order_by('first_name')
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(Q(first_name__icontains=search_query) |
                                       Q(last_name__icontains=search_query) |
                                       Q(email__icontains=search_query))
        return queryset


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "users/user_update.html"
    form_class = UserUpdateForm
    model = Users

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.data = form.data.copy()
        if self.request.method == 'POST':
            email = self.request.POST.get('email')
            if email:
                form.data['user_name'] = email
        return form

    def form_valid(self, form):
        user = form.save(commit=False)
        if self.request.POST.get('email'):
            user.user_name = form.cleaned_data["email"]
        if self.request.POST.get('password1'):
            user.set_password(form.cleaned_data["password1"])
        if self.request.POST.get('allow_signin'):
            user.is_active = True
        else:
            user.is_active = False
        user.save()

        # Get permission codenames
        perm_view_case = Permission.objects.get(codename='can_view_cases')
        perm_edit_case = Permission.objects.get(codename='can_edit_cases')
        perm_view_client = Permission.objects.get(codename='can_view_clients')
        perm_edit_client = Permission.objects.get(codename='can_edit_clients')
        perm_manage_invoice = Permission.objects.get(codename='manage_invoices')
        perm_manage_users = Permission.objects.get(codename='manage_users')

        # Check for permissions and if true, assign the permission
        if self.request.POST.get('view_cases'):
            print("Has View Cases")
            user.user_permissions.add(perm_view_case)
        else:
            user.user_permissions.remove(perm_view_case)

        if self.request.POST.get('edit_cases'):
            user.user_permissions.add(perm_edit_case)
        else:
            user.user_permissions.remove(perm_edit_case)

        if self.request.POST.get('view_clients'):
            user.user_permissions.add(perm_view_client)
        else:
            user.user_permissions.remove(perm_view_client)

        if self.request.POST.get('edit_clients'):
            user.user_permissions.add(perm_edit_client)
        else:
            user.user_permissions.remove(perm_edit_client)

        if self.request.POST.get('manage_invoices'):
            user.user_permissions.add(perm_manage_invoice)
        else:
            user.user_permissions.remove(perm_manage_invoice)

        if self.request.POST.get('manage_users'):
            user.user_permissions.add(perm_manage_users)
        else:
            user.user_permissions.remove(perm_manage_users)

        return redirect(self.get_success_url())
    
    def form_invalid(self, form):
        print("Form is invalid. Errors:")
        for field, errors in form.errors.items():
            for error in errors:
                print(f"{field}: {error}")
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("users:user-list")
