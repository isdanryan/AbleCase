from django.shortcuts import redirect, reverse, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cases, Communications
from .forms import CaseForm, CommunicationForm
from django.views import generic


class CaseListView(LoginRequiredMixin, generic.ListView):
    template_name = "cases/cases_list.html"
    queryset = Cases.objects.all()
    context_object_name = "cases"


class CaseCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "cases/cases_create.html"
    form_class = CaseForm

    def get_success_url(self):
        return reverse("cases:case-list")


@login_required
def CaseDetail(request, pk):
    case = Cases.objects.get(id=pk)
    communications = Communications.objects.filter(case=case).order_by('-date')
    form = CommunicationForm(instance=case)
    if request.method == "GET":
        context = {
            "case": case,
            "communications": communications,
            "form": form,
        }
    if request.method == "POST":
        form = CommunicationForm(request.POST)
        if form.is_valid():
            communication = form.save(commit=False)
            communication.case = case  # Associate entry with the case
            communication.save()
            # Redirect and set marker to to trigger javascript function
            # and take user back to the communications tab
            return redirect(request.path + "?comms=true")
        else:
            print(case.id)
            print(form.errors)  # Check for errors in form validation
        context = {
            "case": case,
            "communications": communications,
            "form": form,
        }
    return render(request, "cases/cases_detail.html", context)


class CaseUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "cases/cases_update.html"
    queryset = Cases.objects.all()
    form_class = CaseForm
    context_object_name = "case"

    def get_success_url(self):
        return reverse("cases:case-list")


@login_required
def CaseDelete(request, pk):
    case = Cases.objects.get(id=pk)
    case.delete()
    return redirect("/cases")
