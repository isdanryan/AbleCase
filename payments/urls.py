from django.urls import path
from .views import create_checkout_session, SuccessView, CancelledView, \
   stripe_webhook

app_name = "payments"

urlpatterns = [
   path('checkout/<int:pk>/', create_checkout_session, name='checkout'),
   path('success/', SuccessView.as_view(), name="success"),
   path('cancelled/', CancelledView.as_view(), name="cancelled"),
   path('webhook/', stripe_webhook, name='stripe-webhook'),
]
