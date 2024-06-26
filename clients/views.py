from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Clients
from .forms import ClientForm
from django.views import generic
from ablecase.mixins import RoleRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator


# Create list of clients
class ClientListView(LoginRequiredMixin, RoleRequiredMixin,
                     generic.ListView):
    template_name = "clients/client_list.html"
    queryset = Clients.objects.all()
    context_object_name = "clients"
    paginate_by = 20
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
            queryset = queryset.filter(Q(display_name__icontains=search_query) |
                                       Q(email__icontains=search_query) |
                                       Q(phone__icontains=search_query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['filter'] = self.request.GET.get('filter')

        # Paginate the queryset
        obj = self.get_queryset()
        paginator = Paginator(obj, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        # Create range to use in layout of pagination
        context['page_range'] = range(1, (page_obj.paginator.num_pages + 1))

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
