from django.urls import path
from .views import client_list, client_create

app_name = "clients"

urlpatterns = [
   path('', client_list),
   path('create/', client_create),
]
