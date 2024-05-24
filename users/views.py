from django.shortcuts import redirect, reverse, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Users
from .forms import UserCreateForm
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
        user.is_active = True
        user.is_staff = True
        user.save()
        messages.success(self.request, 'User created successfully.')
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
        queryset = Users.objects.filter(Q(role='Staff') | Q(role='Admin'))
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(first_name__icontains=search_query)
        return queryset
    

class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "users/user_update.html"
    queryset = Users.objects.all()
    form_class = UserCreateForm
    context_object_name = "user"

    def get_success_url(self):
        return reverse("users:user-list")