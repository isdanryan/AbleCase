from django.urls import path
from .views import InvoiceListView, InvoiceCaseView, CreateInvoice, \
   pdf_view, InvoiceUpdateView

app_name = "invoices"

urlpatterns = [
   path('', InvoiceListView.as_view(), name="invoice-list"),
   path('case/', InvoiceCaseView.as_view(), name="invoice-case-select"),
   path('case/<int:pk>/create', CreateInvoice, name="invoice-create"),
   path('<int:pk>/update', InvoiceUpdateView.as_view(), name="invoice-update"),
   path('print/<int:pk>', pdf_view, name="print-pdf"),
]
