from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Clients
from .forms import ClientForm
from django.views import generic


class ClientListView(LoginRequiredMixin, generic.ListView):
    template_name = "clients/client_list.html"
    queryset = Clients.objects.all()
    context_object_name = "clients"

    def get_queryset(self):
        queryset = Clients.objects.all()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(display_name__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context


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
