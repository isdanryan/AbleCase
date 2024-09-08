from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test.client import RequestFactory
from clients.models import Clients

# Create your tests here.

User = get_user_model()


class PortalSignupViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a client instance for testing
        cls.client_reference = 'TESTREF123'
        cls.client_profile = Clients.objects.create(
            client_reference=cls.client_reference,
            email='testclient@example.com'
        )
        cls.factory = RequestFactory()
        cls.signup_url = reverse('client_portal:client-signup')

    def test_signup_success(self):
        """Test successful signup with valid client reference."""
        data = {
            'email': self.client_profile.email,
            'client_reference': self.client_reference,
            'password1': 'Strongpassword123',
            'password2': 'Strongpassword123'
        }
        response = self.client.post(self.signup_url, data, follow=True)

        # Check that the user was created
        self.assertEqual(User.objects.filter
                         (email=self.client_profile.email).count(), 1)

        # Check that the client was updated with a portal account
        self.client_profile.refresh_from_db()
        self.assertTrue(self.client_profile.portal_account,
                        'Client not given portal account')

        # Check for a successful redirect to the client account page
        self.assertRedirects(response,
                             f'/portal/{self.client_profile.pk}/myaccount/')

    def test_invalid_client_reference(self):
        """Test that an invalid client reference shows an error message."""
        data = {
            'email': 'invalidclient@reference.com',
            'client_reference': 'INVALIDREF123',
            'password1': 'Strongpassword123',
            'password2': 'Strongpassword123'
        }
        response = self.client.post(self.signup_url, data)

        # Check that no user was created
        self.assertEqual(User.objects.filter
                         (email='newuser@example.com').count(), 0)

        # Check for the error message in the response context
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any('The client reference number doesn\'t exist.'
                            in str(m) for m in messages))

    def test_invalid_form_data(self):
        """Test that an invalid form (missing fields) returns errors."""
        data = {
            'email': 'invalidemail',
            'client_reference': self.client_reference,
            'password1': 'short',
            'password2': 'short'
        }
        response = self.client.post(self.signup_url, data)

        # Check that no user was created due to form errors
        self.assertEqual(User.objects.filter(email='invalidemail').count(), 0)

        # Check that the response context contains form errors
        self.assertContains(response, "Enter a valid email address")
        self.assertContains(response, "This password is too short.")
