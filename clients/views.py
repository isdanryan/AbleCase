from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Clients
from .forms import ClientForm
from django.views import generic
from ablecase.mixins import RoleRequiredMixin


# Create list of clients
class ClientListView(LoginRequiredMixin, RoleRequiredMixin,
                     generic.ListView):
    template_name = "clients/client_list.html"
    queryset = Clients.objects.all()
    context_object_name = "clients"
    # Only allow access if users role is staff
    required_role = "Staff"

    # Create search function to search clients display name
    def get_queryset(self):
        queryset = Clients.objects.all()
        search_query = self.request.GET.get('search', '')
        filter = self.request.GET.get('filter')

        # Check for filter
        if filter == 'active':
            queryset = queryset.filter(status='Active')
        elif filter == 'inactive':
            queryset = queryset.filter(status='Inactive')

        if search_query:
            queryset = queryset.filter(display_name__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['filter'] = self.request.GET.get('filter')
        return context


# Create a new client
class ClientCreateView(LoginRequiredMixin, RoleRequiredMixin,
                       generic.CreateView):
    template_name = "clients/client_create.html"
    form_class = ClientForm
    # Only allow access if users role is staff
    required_role = "Staff"

    def get_success_url(self):
        return reverse("clients:client-list")


# Show details of selected client
class ClientDetailView(LoginRequiredMixin, RoleRequiredMixin,
                       generic.DetailView):
    template_name = "clients/client_detail.html"
    queryset = Clients.objects.all()
    context_object_name = "client"
    # Only allow access if users role is staff
    required_role = "Staff"


# View to update clients details
class ClientUpdateView(LoginRequiredMixin, RoleRequiredMixin,
                       generic.UpdateView):
    template_name = "clients/client_update.html"
    queryset = Clients.objects.all()
    form_class = ClientForm
    context_object_name = "client"
    # Only allow access if users role is staff
    required_role = "Staff"

    def get_success_url(self):
        return reverse("clients:client-list")
