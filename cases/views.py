from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Cases
from .forms import CaseForm
from django.views import generic


class CaseListView(generic.ListView):
    template_name = "cases/cases_list.html"
    queryset = Cases.objects.all()
    context_object_name = "cases"
