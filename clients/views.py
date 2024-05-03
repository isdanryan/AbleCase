from django.shortcuts import render
from django.http import HttpResponse
from .models import Clients


def client_list(request):
    clients = Clients.objects.all()
    context = {
        "clients": clients
    }
    return render(request, "clients/client_list.html", context)
