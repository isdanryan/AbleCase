from django.urls import path
from .views import UserLogin, UserSignOut

app_name = 'authentication'

urlpatterns = [
   path('', UserLogin, name="login"),
   path('signout/', UserSignOut, name='signout'),
]
