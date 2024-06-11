from django.urls import path
from .views import ClientLoginView, ClientAccountView, PortalSignup, ClientSignOut, ClientInvoiceList

app_name = "client_portal"

urlpatterns = [
   ## Find payment
   ## Make payment 
   path('myinvoices/', ClientInvoiceList.as_view(), name="client-invoices" ),
   path('login/', ClientLoginView, name="client-login"),
   path('register/', PortalSignup, name="client-signup"),
   path('<int:pk>/myaccount/', ClientAccountView.as_view(), name="client-account"),
   path('signout', ClientSignOut, name="signout")
]
