from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from .models import Cases, Communications, CaseTypes
from clients.models import Clients
from invoices.models import InvoiceCode
from django.utils import timezone

User = get_user_model()


class CaseViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a user and some cases for testing."""
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
            codename='can_view_cases')
            )
        cls.user.user_permissions.add(Permission.objects.get(
            codename='can_edit_cases')
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
        cls.case1 = Cases.objects.create(
            case_number=12345,
            case_name='Test Case 1',
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

    def setUp(self):
        self.client = Client()
        self.client.login(email='staffuser@example.com',
                          password='testpassword')

    # Test the list view displays the cases
    def test_case_list_view(self):
        """Test the case list view."""
        response = self.client.get(reverse('cases:case-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 12345)

    def test_case_create_view(self):
        """Test creating a new case."""
        # Define the data for creating a case
        data = {
            'case_number': 56789,
            'case_name': 'Test Case 2',
            'type': self.case_type.id,
            'invoice_code': self.invoice_code.id,
            'address': '456 Test Street, Test City, TC45 6TC',
            'phone': '07781386623',
            'review_date': timezone.now().date(),
            'assigned': 'Stephen Hawkings',
            'status': 'Open',
            'notes': 'Initial case notes.',
            'client': self.client1.id,
        }

        # Send a POST request to the create view with the data
        response = self.client.post(reverse('cases:case-create'), data)

        # Check if the response status code is 302,
        # redirection after successful creation
        self.assertEqual(response.status_code, 302)

        # Verify that the case was created in the database
        case = Cases.objects.get(case_number=56789)
        self.assertEqual(case.case_name, 'Test Case 2')
        self.assertEqual(case.type, self.case_type)
        self.assertEqual(case.invoice_code, self.invoice_code)
        self.assertEqual(case.address, '456 Test Street, Test City, TC45 6TC')
        self.assertEqual(case.phone, '+447781386623')
        self.assertEqual(case.assigned, 'Stephen Hawkings')
        self.assertEqual(case.status, 'Open')
        self.assertEqual(case.client, self.client1)

    # Test the detail view for a case
    def test_case_detail_view(self):
        """Test viewing case details and adding a communication."""
        response = self.client.get(reverse('cases:case-details',
                                           args=[self.case1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Case 1')

        # Add a communication
        communication_data = {
            'details': 'This is a test communication',
            'date': timezone.now().date()
        }
        response = self.client.post(
            reverse(
                'cases:case-details', args=[self.case1.id]
                ),
            communication_data)

        # Check for redirect after post
        self.assertEqual(response.status_code, 302)

        # Check record exists
        self.assertTrue(Communications.objects.filter(
            details='This is a test communication').exists())

    def test_case_update_view(self):
        """Test updating an existing case."""
        data = {
            'case_number': 12345,
            'case_name': 'Test Case 1 Updated',
            'type': self.case_type.id,
            'invoice_code': self.invoice_code.id,
            'address': '123 Test Street, Test City, TC12 3TC',
            'phone': '07784286541',
            'review_date': timezone.now().date(),
            'assigned': 'John Doe',
            'status': 'Closed',
            'notes': 'Initial case notes.',
            'client': self.client1.id,
        }
        response = self.client.post(
            reverse(
                'cases:case-update', args=[self.case1.id]
                ),
            data)

        # Check for a successful redirect after post
        self.assertEqual(response.status_code, 302)

        # Refresh case 1 data from db
        self.case1.refresh_from_db()

        # Check updated details
        self.assertEqual(self.case1.case_name, 'Test Case 1 Updated')
        self.assertEqual(self.case1.status, 'Closed')

    # Test a case can be deleted
    def test_case_delete_view(self):
        """Test deleting a case."""
        response = self.client.post(reverse('cases:case-delete',
                                            args=[self.case1.id]))

        # Redirect after successful deletion
        self.assertEqual(response.status_code, 302)

        # Check case no longer exisits
        self.assertFalse(Cases.objects.filter(id=self.case1.id).exists())
