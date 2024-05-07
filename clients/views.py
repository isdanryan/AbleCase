from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Clients
from .forms import ClientForm
from django.views import generic


# def client_list(request):
#     clients = Clients.objects.all()
#     context = {
#         "clients": clients
#     }
#     return render(request, "clients/client_list.html", context)

class ClientListView(generic.ListView):
    template_name = "clients/client_list.html"
    queryset = Clients.objects.all()
    context_object_name = "clients"


class ClientCreateView(generic.CreateView):
    template_name = "clients/client_create.html"
    form_class = ClientForm

    def get_success_url(self):
        return reverse("clients:client-list")


class ClientDetailView(generic.DetailView):
    template_name = "clients/client_detail.html"
    queryset = Clients.objects.all()
    context_object_name = "client"


class ClientUpdateView(generic.UpdateView):
    template_name = "clients/client_update.html"
    queryset = Clients.objects.all()
    form_class = ClientForm

    def get_success_url(self):
        return reverse("clients:client-list")


class ClientDeleteView(generic.DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Clients.objects.all()
    context_object_name = "client"


def ClientDelete(request, pk):
    client = Clients.objects.get(id=pk)
    client.delete()
    return redirect("/clients")
