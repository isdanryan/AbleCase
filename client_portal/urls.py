from django.urls import path
from .views import ClientLoginView, ClientAccountView, PortalSignup, \
   ClientSignOut, ClientInvoiceList, ClientPaymentsList

app_name = "client_portal"

urlpatterns = [
   path('myinvoices/', ClientInvoiceList.as_view(), name="client-invoices"),
   path('mypayments/', ClientPaymentsList.as_view(), name="client-payments"),
   path('login/', ClientLoginView, name="client-login"),
   path('', ClientLoginView, name="default-login"),
   path('register/', PortalSignup, name="client-signup"),
   path('<int:pk>/myaccount/', ClientAccountView.as_view(),
        name="client-account"),
   path('signout', ClientSignOut, name="signout")
]
