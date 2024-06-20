from django.urls import path
from .views import UserCreateView, UserListView, UserUpdateView, UserProfileView

app_name = "users"

urlpatterns = [
   path('', UserListView.as_view(), name="user-list"),
   path('create/', UserCreateView.as_view(), name="user-create"),
   path('<int:pk>/update/', UserUpdateView.as_view(), name="user-update"),
   path('profile/', UserProfileView.as_view(), name="user-profile"),
]
