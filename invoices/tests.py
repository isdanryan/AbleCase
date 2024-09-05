from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from cases.models import Cases, CaseTypes
from clients.models import Clients
from .models import InvoiceCode, Invoices
from django.utils import timezone

User = get_user_model()


class InvoicesViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a user, cases and invoices for testing."""
        # Create a user with Staff role
        cls.user = User.objects.create_user(
            first_name='active',
            last_name='staffuser',
            email='staffuser@example.com',
            password='testpassword',
            role='Staff',
            is_active=True
            )
        cls.user.user_permissions.add(Permission.objects.get(
            codename='manage_invoices')
            )

        # Create a client
        cls.client1 = Clients.objects.create(
            display_name='Client A',
            phone='07762815507',
            email='clienta@example.com',
            status='Active',
            type='Individual',
            client_reference='A12122314231'
        )

        # Create a case type instance for testing
        cls.case_type = CaseTypes.objects.create(type='General Inquiry')

        # Create an invoice code instance for testing
        cls.invoice_code = InvoiceCode.objects.create(short_code='EV',
                                                      name='Eviction')

        # Create a case for testing
        cls.case2 = Cases.objects.create(
            case_number=12345,
            case_name='Test Case 2',
            type=cls.case_type,
            invoice_code=cls.invoice_code,
            address='123 Test Street, Test City, TC12 3TC',
            phone='07784286541',
            review_date=timezone.now().date(),
            assigned='John Doe',
            status='Open',
            notes='Initial case notes.',
            client=cls.client1,
        )

        cls.case3 = Cases.objects.create(
            case_number=56789,
            case_name='Test Case 3',
            type=cls.case_type,
            invoice_code=cls.invoice_code,
            address='456 Test Street, Test City, TC45 6TC',
            phone='07784286541',
            review_date=timezone.now().date(),
            assigned='Stephen Hawkings',
            status='Open',
            notes='Initial case notes.',
            client=cls.client1,
        )

        # Create an invoice from above case
        cls.invoice1 = Invoices.objects.create(
            invoice_number=1001,
            date=timezone.now().date(),
            term='On Reciept',
            date_due=timezone.now().date(),
            amount=100.00,
            vat="20%",
            total_due=120.00,
            case=cls.case2,
            case_address=cls.case2.address,
            case_type=cls.case2.type,
            case_name=cls.case2.case_name,
            invoice_code=cls.case2.invoice_code,
            client=cls.case2.client,
            status=cls.case2.status,
            notes=cls.case2.notes,
        )

    def setUp(self):
        """Initialize the client for each test method."""
        self.client = Client()
        self.client.login(email='staffuser@example.com',
                          password='testpassword')

    # Test the list view displays the invoices
    def test_invoice_list_view(self):
        """Test the invoice list view."""
        response = self.client.get(reverse('invoices:invoice-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 1001)

    def test_invoice_update_view(self):
        """Test that the detail and update view works for invoices"""
        # Set the updated invoice data
        data = {
            'invoice_number': 1001,
            'date': timezone.now().date(),
            'term': 'On Receipt',
            'date_due': timezone.now().date(),
            'amount': 200.00,
            'vat': "20%",
            'total_due': 240.00,
            'case': self.case2.id,
            'case_address': self.case2.address,
            'case_type': self.case2.type,
            'case_name': self.case2.case_name,
            'invoice_code': self.case2.invoice_code,
            'client': self.case2.client.id,
            'status': 'Paid',  # Update status
            'notes': self.case2.notes
        }

        # Submit the update to the view
        response = self.client.post(reverse('invoices:invoice-update',
                                            args=[self.invoice1.id]), data)
        # Check for successful redirect after post
        self.assertEqual(response.status_code, 302)
        self.invoice1.refresh_from_db()

        # Check the updated invoice shows in the db
        updated_invoice = Invoices.objects.get(id=self.invoice1.id)
        self.assertEqual(updated_invoice.status, 'Paid')

    # Test an invoice can be created
    def test_invoice_create_view(self):
        """Test creating a new invoice"""
        # Define the invoice to be created
        data = {
            'invoice_number': 1002,
            'date': timezone.now().date(),
            'term': 'On Receipt',
            'date_due': timezone.now().date(),
            'amount': 200.00,
            'vat': "20%",
            'total_due': 240.00,
            'case': self.case3.id,
            'case_address': self.case3.address,
            'case_type': self.case3.type,
            'case_name': self.case3.case_name,
            'invoice_code': self.case3.invoice_code,
            'client': self.case3.client.id,
            'status': 'Sent',
            'notes': self.case3.notes
        }

        # Post the new data to the create view
        response = self.client.post(reverse('invoices:invoice-create',
                                            args=[self.case3.id]), data)

        # Check for a successful redirect
        self.assertEqual(response.status_code, 302)

        # Check the new invoice is in the database
        invoice = Invoices.objects.get(invoice_number=1002)
        self.assertEqual(invoice.case_name, self.case3.case_name)
