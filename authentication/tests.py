from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages

# Get the custom user model
User = get_user_model()


class AuthenticationViewsTests(TestCase):

    def setUp(self):
        # Create an active test staff user
        self.active_staff_user = User.objects.create_user(
            first_name='active',
            last_name='staffuser',
            email='active_staffuser@example.com',
            password='testpassword',
            role='Staff',
            is_active=True
        )
        self.active_staff_user.save()

        # Create an inactive test staff user
        self.inactive_staff_user = User.objects.create_user(
            first_name='inactive',
            last_name='staffuser',
            email='inactive_staffuser@example.com',
            password='testpassword',
            role='Staff',
            is_active=False
        )
        self.inactive_staff_user.save()

    # Test a successful login
    def test_user_login_success(self):
        """Test successful login for a staff user."""
        response = self.client.post(reverse('authentication:login'), {
            'username': 'active_staffuser@example.com',
            'password': 'testpassword'
        })

        # Check for redirection after login
        self.assertEqual(response.status_code, 302)

        # Check user is correctly redirected to the dashboard
        self.assertRedirects(response, '/')

        # And that they are authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    # Test a login with invalid credentials
    def test_user_login_invalid_credentials(self):
        """Test unsuccessful login with invalid credentials."""
        response = self.client.post(reverse('authentication:login'), {
            'username': 'active_staffuser@example.com',
            'password': 'wrongpassword'
        })

        # Check that the user isn't redirected
        self.assertEqual(response.status_code, 200)

        # Get messages and check the correct message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            message.message == "Incorrect username or password"
            for message in messages
            ))

    # Test to make sure a user marked as inactive, can't login
    def test_inactive_user_login(self):
        """Test unsuccessful login for a non-staff user."""
        response = self.client.post(reverse('authentication:login'), {
            'username': 'inactive_staffuser@example.com',
            'password': 'testpassword'
        })

        # Check that the user isn't redirected
        self.assertEqual(response.status_code, 200)

        # Get messages and check the correct message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            message.message == "Incorrect username or password"
            for message in messages
            ))

    # Test an already logged in user is redirected
    def test_user_login_redirect_if_authenticated(self):
        """Test redirection to dashboard if user is already authenticated."""
        self.client.login(email='active_staffuser@example.com',
                          password='testpassword')
        response = self.client.get(reverse('authentication:login'))
        self.assertRedirects(response, '/')  # Redirect to the dashboard

    # Test user logout process
    def test_user_logout(self):
        """Test successful logout and redirection to the login page."""
        self.client.login(email='active_staffuser@example.com',
                          password='testpassword')
        response = self.client.get(reverse('authentication:signout'))
        self.assertEqual(response.status_code, 302)  # Check for redirect

        # Check final location is login page
        self.assertEqual(response['Location'], '/login')

        # Check user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)
