from django.urls import path
from .views import ClientLoginView, ClientAccountView, PortalSignup

app_name = "client_portal"

urlpatterns = [
   ## Find payment
   ## Make payment 
   path('login/', ClientLoginView, name="client-login"),
   path('register/', PortalSignup, name="client-signup"),
   path('<int:pk>/myaccount/', ClientAccountView.as_view(), name="client-account"),
]
