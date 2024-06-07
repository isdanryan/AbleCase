from django.urls import path
from .views import UserCreateView, UserListView, UserUpdateView

app_name = "users"

urlpatterns = [
   path('', UserListView.as_view(), name="user-list"),
   path('create/', UserCreateView.as_view(), name="user-create"),
   path('<int:pk>/update/', UserUpdateView.as_view(), name="user-update"),
]
