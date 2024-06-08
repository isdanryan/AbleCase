from django.shortcuts import redirect, reverse, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from clients.models import Clients
from users.models import Users
from .forms import ClientForm, ClientLoginForm, PortalSignupForm
from django.views import generic



class ClientAccountView(LoginRequiredMixin, generic.DetailView):
    template_name = "client_portal/account_details.html"
    queryset = Clients.objects.all()
    context_object_name = "account_details"


def ClientLoginView(request):
    if not request.user.is_authenticated:
        form = ClientLoginForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    if user.role == "Client":
                        try:
                            client_id = user.client.pk
                            login(request, user)
                            print(request, "Login successful")
                            return redirect(f'/portal/{client_id}/myaccount')
                        except Clients.DoesNotExist:
                            messages.error(request, "Associated client profile not found")
                    else:
                        messages.error(request, "You are not a client")
                else:
                    messages.error(request, "Incorrect Username or password")

        return render(request, 'client_portal/portal_login.html', {'form': form})
    else:
        return redirect("/")


def UserSignOut(request):
    logout(request)
    return redirect('/login')


def PortalSignup(request):
    if request.method == 'POST':
        form = PortalSignupForm(request.POST)
        if form.is_valid():
            # Retrieve the client profile based on the provided reference number
            email = form.cleaned_data['email']
            client_reference = form.cleaned_data['client_reference']
            password = form.cleaned_data['password1']

            user = Users.objects.create_user(email=email, password=password, first_name='', last_name='', role='Client', is_active=True)

            client = Clients.objects.get(client_reference=client_reference)

            if not client.email:
                client.email = email

            client.portal_account = user
            client.has_portal_access = True
            client.save()

            login(request, user)
            return redirect(f'/portal/{client.pk}/myaccount')
        else:
            print(form.errors)
    else:
        form = PortalSignupForm()
    return render(request, 'client_portal/portal_register.html', {'form': form})


def ClientSignOut(request):
    logout(request)
    return redirect('/portal/login')
