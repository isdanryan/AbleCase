from django.urls import path
from .views import (CaseListView, CaseCreateView, CaseUpdateView,
                    CaseDelete, CaseDetail)

app_name = "cases"

urlpatterns = [
   path('', CaseListView.as_view(), name="case-list"),
   path('create/', CaseCreateView.as_view(), name="case-create"),
   path('<int:pk>/', CaseDetail, name="case-details"),
   path('<int:pk>/update/', CaseUpdateView.as_view(), name="case-update"),
   path('<int:pk>/delete/', CaseDelete, name="case-delete"),
]
