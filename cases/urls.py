from django.urls import path
from .views import CaseListView

app_name = "cases"

urlpatterns = [
   path('', CaseListView.as_view(), name="case-list"),
]