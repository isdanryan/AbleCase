from django.shortcuts import redirect, reverse, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cases, Communications
from .forms import CaseForm, CommunicationForm
from django.views import generic
from ablecase.decorators import role_required
from ablecase.mixins import RoleRequiredMixin


# Create list of cases
class CaseListView(LoginRequiredMixin, RoleRequiredMixin, generic.ListView):
    template_name = "cases/cases_list.html"
    queryset = Cases.objects.all()
    context_object_name = "cases"
    required_role = "Staff"

    def get_queryset(self):
        queryset = Cases.objects.all()
        search_query = self.request.GET.get('search', '')
        filter = self.request.GET.get('filter')

        # Check for filter
        if filter == 'open':
            queryset = queryset.filter(status='Open')
        elif filter == 'closed':
            queryset = queryset.filter(status='Closed')

        # Check for a search param
        if search_query:
            queryset = queryset.filter(case_number__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['filter'] = self.request.GET.get('filter')
        return context


# Create a new case
class CaseCreateView(LoginRequiredMixin, RoleRequiredMixin, generic.CreateView):
    template_name = "cases/cases_create.html"
    form_class = CaseForm
    required_role = "Staff"

    def get_success_url(self):
        return reverse("cases:case-list")


# Displays details for selected case
@login_required
@role_required("Staff")
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
    # Add addtional communication records to the current case    
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


# Update the current case
class CaseUpdateView(LoginRequiredMixin, RoleRequiredMixin,
                     generic.UpdateView):
    template_name = "cases/cases_update.html"
    queryset = Cases.objects.all()
    form_class = CaseForm
    context_object_name = "case"
    required_role = "Staff"

    def get_success_url(self):
        return reverse("cases:case-list")


# Delete the selected case
@login_required
@role_required("Staff")
def CaseDelete(request, pk):
    case = Cases.objects.get(id=pk)
    case.delete()
    return redirect("/cases")
