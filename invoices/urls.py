from django.urls import path
from .views import InvoiceListView, InvoiceCaseView, CreateInvoice

app_name = "invoices"

urlpatterns = [
   path('', InvoiceListView.as_view(), name="invoice-list"),
   path('case/', InvoiceCaseView.as_view(), name="invoice-case-select"),
   path('case/<int:pk>/create', CreateInvoice, name="invoice-create")
]
