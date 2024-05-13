from django.urls import path
from .views import CaseListView, CaseCreateView, CaseDetailView, CaseUpdateView, CaseDelete

app_name = "cases"

urlpatterns = [
   path('', CaseListView.as_view(), name="case-list"),
   path('create/', CaseCreateView.as_view(), name="case-create"),
   path('<int:pk>/', CaseDetailView.as_view(), name="case-details"),
   path('<int:pk>/update/', CaseUpdateView.as_view(), name="case-update"),
   path('<int:pk>/delete/', CaseDelete, name="case-delete"),
]
