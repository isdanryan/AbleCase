from django.urls import path
from .views import InvoiceCreateView

app_name = "invoices"

urlpatterns = [
   path('create/', InvoiceCreateView.as_view(), name="invoice-create"),
]
