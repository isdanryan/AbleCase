from typing import Any
from django.forms import BaseModelForm
from django.shortcuts import render, reverse
from django.views import generic
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from cases.models import Cases
from users.models import Tasks
from users.forms import UserTaskForm


class DashboardView(LoginRequiredMixin, generic.CreateView):
    template_name = "dashboard/dashboard.html"
    form_class = UserTaskForm
    model = Tasks

    def get_success_url(self):
        return reverse('dashboard:dashboard') 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['review_cases'] = Cases.objects.filter(review_date__lt=date.today())
        context['total_review'] = context['review_cases'].count()
        context['total_open_cases'] = Cases.objects.filter(status='Open').count()
        context['total_cases'] = Cases.objects.count()
        current_user = self.request.user
        context['tasks'] = Tasks.objects.filter(user=current_user)
        return context
