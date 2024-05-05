from django.urls import path
from .views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView

app_name = "clients"

urlpatterns = [
   path('', ClientListView.as_view(), name="client-list"),
   path('<int:pk>/', ClientDetailView.as_view(), name="client-details"),
   path('<int:pk>/update/', ClientUpdateView.as_view(), name="client-update"),
   path('create/', ClientCreateView.as_view(), name="client-create"),
]
