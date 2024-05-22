from django.urls import path
from .views import UserLogin

app_name = 'authentication'

urlpatterns = [
   path('', UserLogin, name="login"),
]
