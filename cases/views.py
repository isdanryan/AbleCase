from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Cases
from .forms import CaseForm
from django.views import generic


class CaseListView(generic.ListView):
    template_name = "cases/cases_list.html"
    queryset = Cases.objects.all()
    context_object_name = "cases"


class CaseCreateView(generic.CreateView):
    template_name = "cases/cases_create.html"
    form_class = CaseForm

    def get_success_url(self):
        return reverse("cases:case-list")


class CaseDetailView(generic.DetailView):
    template_name = "cases/cases_detail.html"
    queryset = Cases.objects.all()
    context_object_name = "case"


class CaseUpdateView(generic.UpdateView):
    template_name = "cases/cases_update.html"
    queryset = Cases.objects.all()
    form_class = CaseForm

    def get_success_url(self):
        return reverse("cases:case-list")


def CaseDelete(request, pk):
    case = Cases.objects.get(id=pk)
    case.delete()
    return redirect("/cases")
