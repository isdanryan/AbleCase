from django.shortcuts import render
from django.http import HttpResponse


def client_list(request):
    return render(request, "clients/client_list.html")
