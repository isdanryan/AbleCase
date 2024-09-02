from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from clients.models import Clients
from users.models import Users
from invoices.models import Invoices
from payments.models import Payment
from .forms import (ClientLoginForm,
                    PortalSignupForm, PasswordResetForm)
from django.views import generic
from ablecase.mixins import RoleRequiredMixin
from django.views.generic.edit import FormMixin
from ablecase.decorators import role_required
from django.core.paginator import Paginator


class ClientAccountView(LoginRequiredMixin, RoleRequiredMixin,
                        FormMixin, generic.DetailView):
    template_name = "client_portal/account_details.html"
    form_class = PasswordResetForm
    # Require user has client role
    required_role = "Client"

    # Overide get method to handle both displaying details
    # and getting new password
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    # Overide post method to handle password update
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # Stop form from saving automatically
            form.save(commit=False)
            # Get current user and set new password from form data
            user = self.request.user
            user.set_password(form.cleaned_data["new_password1"])
            user.save()
            messages.success(
                request,
                "Your password has been updated. \
                Please log back in using the new password."
                )
            # Redirect to signout to force user to login with new password
            return redirect('/portal/signout')
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_object(self):
        # Retrieve the user instance to be updated
        return get_object_or_404(Users, pk=self.kwargs['pk'])

    # Pass additional arguements to the form
    def get_form_kwargs(self):
        # Get Django's default keywords for the FormMixin
        kwargs = super().get_form_kwargs()
        # Get the user instance
        kwargs['user'] = self.get_object()
        return kwargs

    # Handle the required context to display
    def get_context_data(self, **kwargs):
        # Set to the current logged in user
        current_user = self.request.user
        # Prep the context container
        context = super().get_context_data(**kwargs)
        # Pass in the info to display the form
        context['form'] = kwargs.get('form', self.get_form())
        # Get the details based off current user
        # and pass into the context container
        context['account_details'] = Clients.objects.get(
            portal_account=current_user
            )
        context['users'] = Users.objects.get(email=current_user)
        return context


# Login view for client portal
def ClientLoginView(request):
    # Check if the client is already logged in
    if not request.user.is_authenticated:
        form = ClientLoginForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username,
                                    password=password)

                # Check user exists and has the correct role
                if user is not None:
                    if user.role == "Client":
                        # Attempt login with the supplied details
                        try:
                            client_id = user.id
                            login(request, user)
                            print(request, "Login successful")
                            return redirect(f'/portal/{client_id}/myaccount')
                        # Handle error states
                        except Clients.DoesNotExist:
                            messages.error(
                                request,
                                "Associated client profile not found"
                                )
                    else:
                        messages.error(request, "You are not a client")
                else:
                    messages.error(request, "Incorrect Username or password")
        # Send user to login page by default
        return render(request, 'client_portal/portal_login.html',
                      {'form': form})
    else:
        # If already logged in redirect to clients account page
        client_id = request.user.id
        return redirect(f'/portal/{client_id}/myaccount')


# View to allow client to register on the portal
def PortalSignup(request):
    # Check if the client is already logged in 
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = PortalSignupForm(request.POST)
            if form.is_valid():
                # Retrieve the client profile based on
                # the provided reference number
                email = form.cleaned_data['email']
                client_reference = form.cleaned_data['client_reference']
                password = form.cleaned_data['password1']
                # Create user from the entered info, set role to client
                # and overide default active state
                user = Users.objects.create_user(
                    email=email, password=password,
                    first_name='', last_name='',
                    role='Client', is_active=True
                    )

                # Get the client profile that matches the client reference
                client = Clients.objects.get(client_reference=client_reference)

                # If the client profile dosen't have an email address
                # use the one entered at signup
                if not client.email:
                    client.email = email

                # Attach the user account to the client profile
                client.portal_account = user

                # Set so they can use the portal
                client.has_portal_access = True

                client.save()

                # Log the client in and send to their accounts page
                login(request, user)
                return redirect(f'/portal/{client.pk}/myaccount')
            else:
                print(form.errors)
        else:
            form = PortalSignupForm()
        return render(request, 'client_portal/portal_register.html',
                      {'form': form})
    else:
        # If already logged in redirect to clients account page
        client_id = request.user.client.pk
        return redirect(f'/portal/{client_id}/myaccount')


# Sign client out
@role_required("Client")
def ClientSignOut(request):
    logout(request)
    return redirect('/portal/login')


# Build list of client invoices
class ClientInvoiceList(LoginRequiredMixin, RoleRequiredMixin,
                        generic.ListView):
    template_name = "client_portal/client_invoices.html"
    context_object_name = "invoices"
    paginate_by = 20
    required_role = "Client"

    # Create search function to search name or email address
    def get_queryset(self):
        current_user = self.request.user
        queryset = Invoices.objects.filter(client=current_user.client)
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(invoice_number__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')

        # Paginate the queryset
        obj = self.get_queryset()
        paginator = Paginator(obj, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj

        return context
    

# Build list of client invoices
class ClientPaymentsList(LoginRequiredMixin, RoleRequiredMixin,
                         generic.ListView):
    template_name = "client_portal/client_payments.html"
    context_object_name = "payments"
    paginate_by = 20
    required_role = "Client"

    # Create search function to search name or email address
    def get_queryset(self):
        queryset = Payment.objects.filter(user=self.request.user)
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(invoice__number__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')

        # Paginate the queryset
        obj = self.get_queryset()
        paginator = Paginator(obj, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj

        return context
