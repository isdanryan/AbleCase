from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Clients
from .forms import ClientForm


def client_list(request):
    clients = Clients.objects.all()
    context = {
        "clients": clients
    }
    return render(request, "clients/client_list.html", context)


def client_create(request):
    form = ClientForm()
    if request.method == "POST":
        print('Reciving a post request')
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/clients")
    context = {
        "form": form,
    }
    return render(request, "clients/client_create.html", context)