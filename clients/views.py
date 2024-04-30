from django.shortcuts import render
from django.http import HttpResponse


def client_list(request):
    return HttpResponse("This is the list of clients!")
