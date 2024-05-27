from typing import Any
from django.shortcuts import render
from django.views import generic
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from cases.models import Cases


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['review_cases'] = Cases.objects.filter(review_date__lt=date.today())
        context['total_review'] = context['review_cases'].count()
        context['total_open_cases'] = Cases.objects.filter(status='Open').count()
        context['total_cases'] = Cases.objects.count()
        return context