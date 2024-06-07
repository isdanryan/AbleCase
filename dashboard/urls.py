from django.urls import path
from .views import DashboardView, TaskDelete

app_name = "dashboard"

urlpatterns = [
   path('', DashboardView.as_view(), name="dashboard"),
   path('tasks/<int:pk>/delete', TaskDelete, name=("task-delete")),
]
