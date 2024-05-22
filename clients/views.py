from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Clients
from .forms import ClientForm
from django.views import generic


class ClientListView(LoginRequiredMixin, generic.ListView):
    template_name = "clients/client_list.html"
    queryset = Clients.objects.all()
    context_object_name = "clients"


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "clients/client_create.html"
    form_class = ClientForm

    def get_success_url(self):
        return reverse("clients:client-list")


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "clients/client_detail.html"
    queryset = Clients.objects.all()
    context_object_name = "client"


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "clients/client_update.html"
    queryset = Clients.objects.all()
    form_class = ClientForm
    context_object_name = "client"

    def get_success_url(self):
        return reverse("clients:client-list")
