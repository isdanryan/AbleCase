import stripe
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from clients.models import Clients
from invoices.models import Invoices
from .models import Payment
from decouple import config
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from ablecase.mixins import RoleRequiredMixin
from django.contrib.auth.decorators import login_required

stripe.api_key = config('STRIPE_API_KEY')


# Create strip checktou session
@login_required
def create_checkout_session(request, pk):
    invoice = get_object_or_404(Invoices, id=pk)
    checkout_session = stripe.checkout.Session.create(
        # Buid invoice to send to stripe fro checkout
        line_items=[
            {
                "price_data": {
                    "currency": "gbp",
                    "product_data": {
                        "name": f'Invoice {invoice.invoice_number}',
                        },
                    "unit_amount": int(invoice.total_due * 100),
                },
                "quantity": 1,
            }],
        mode='payment',
        success_url=config('DOMAIN') + '/payments/success/',
        cancel_url=config('DOMAIN') + '/payments/cancel/',
        # Include invoice id in metadata to pass to webhook
        metadata={
            'invoice_id': invoice.id
        }
    )
    return redirect(checkout_session.url, code=303)


# Create strip webhook to
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = config('STRIPE_WEBHOOK_SECRET')

    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, endpoint_secret
        )

    # Payload is invalid
    except ValueError as e:
        return HttpResponse(status=400)

    # Signature is invalid
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    # Handle the checkout completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        invoice_id = session['metadata']['invoice_id']
        invoice = Invoices.objects.get(id=invoice_id)
        # Add payment record to database
        Payment.objects.create(
            user=invoice.client.portal_account,
            invoice=invoice,
            amount_payed=invoice.total_due,
            stripe_charge_id=session['payment_intent']
        )
        # Update invoice to paid
        invoice.status = "Paid"
        invoice.save()

    return HttpResponse(status=200)


# Checkout success view
class SuccessView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    template_name = "payments/success.html"

# Checkout cancelled view
class CancelledView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    template_name = "payments/cancel.html"
