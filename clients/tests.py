from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from .models import Clients

User = get_user_model()


class ClientViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a user and some clients for testing."""
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
            codename='can_view_clients')
            )
        cls.user.user_permissions.add(Permission.objects.get(
            codename='can_edit_clients')
            )

        # Create sample clients
        cls.client1 = Clients.objects.create(
            display_name='Client A',
            phone='07762815507',
            email='clienta@example.com',
            status='Active',
            type='Individual',
            client_reference='A12122314231'
        )
        cls.client2 = Clients.objects.create(
            display_name='Client B',
            phone='+0987654321',
            email='clientb@example.com',
            status='Inactive',
            type='Buisness',
            client_reference='B12122314231'
        )

    def setUp(self):
        # Set up the client with authentication
        self.client = Client()
        self.client.login(email='staffuser@example.com',
                          password='testpassword')

    # Test client list view
    def test_client_list_view(self):
        """Test the client list view with pagination and filtering."""
        response = self.client.get(reverse('clients:client-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Client A')
        self.assertContains(response, 'Client B')

    # Test create view works for creating a new client
    def test_client_create_view(self):
        """Test creating a new client."""
        data = {
            'display_name': 'Client C',
            'phone': '01275893621',
            'email': 'clientc@example.com',
            'status': 'Active',
            'type': 'Individual',
            'client_reference': 'C12122314231'
        }

        # Post data to create view
        response = self.client.post(reverse('clients:client-create'), data)

        # Check redirect after submit
        self.assertEqual(response.status_code, 302)

        # Check new client exists in db
        self.assertTrue(Clients.objects.filter(
            display_name='Client C'
            ).exists())

    # Test client detail view works
    def test_client_detail_view(self):
        """Test viewing client details."""
        response = self.client.get(reverse('clients:client-details',
                                           args=[self.client1.id]))

        # Check for success response
        self.assertEqual(response.status_code, 200)

        # Check correct client is displayed
        self.assertContains(response, 'Client A')
        self.assertContains(response, '+447762815507')

    # Test client can be updated
    def test_client_update_view(self):
        """Test updating an existing client."""
        data = {
            'display_name': 'Client A Updated',
            'phone': '07762815507',
            'email': 'clientaupdated@example.com',
            'status': 'Inactive',
            'type': 'Individual',
            'client_reference': 'A12122314231'
        }
        response = self.client.post(reverse('clients:client-update',
                                            args=[self.client1.id]), data)

        # Check successful redirect after post
        self.assertRedirects(response, reverse('clients:client-list'))

        # Refresh data from db
        self.client1.refresh_from_db()

        # Check updated details
        self.assertEqual(self.client1.display_name, 'Client A Updated')
        self.assertEqual(self.client1.email, 'clientaupdated@example.com')
        self.assertEqual(self.client1.status, 'Inactive')
