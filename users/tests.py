from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from .models import Users

User = get_user_model()


class UsersViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a user that case manage other users"""
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
            codename='manage_users')
            )

        # Create a second user for testing
        cls.user2 = User.objects.create_user(
            first_name='second',
            last_name='staffuser',
            email='seconduser@example.com',
            password='testpassword',
            role='Staff',
            is_active=True
            )
        cls.user2.user_permissions.add(Permission.objects.get(
            codename='view_cases')
            )

    def setUp(self):
        self.client = Client()
        self.client.login(email='staffuser@example.com',
                          password='testpassword')

    # Check for the basic list view
    def test_user_list_view(self):
        """Test the users list view show exisiting users"""
        response = self.client.get(reverse('users:user-list'))
        self.assertContains(response, 'second')
        self.assertContains(response, 'staffuser')
        self.assertContains(response, 'seconduser@example.com')

    # Check that a users permissions can be updated
    def test_change_user_permissions(self):
        """Test that permissions can be changed"""
        # Create updated data
        data = {
            'first_name': 'second',
            'last_name': 'updatedname',
            'email': 'seconduser@example.com',
            'password': 'testpassword',
            'role': 'Staff',
            'is_active': True,
            'view_clients': True,  # Add in view clients perm
        }

        # Update user permission
        response = self.client.post(reverse('users:user-update',
                                            args=[self.user2.id]), data)
        self.assertEqual(response.status_code, 302)

        # Get the updated permissions for the user
        user_permissions = self.user2.user_permissions.all()

        # Extract the codenames of the permissions
        user_permission_codenames = [perm.codename
                                     for perm in user_permissions]

        # Check that the added permission is present
        self.assertIn('can_view_clients', user_permission_codenames,
                      'View clients permission not found after update.')

        # Check users updated name
        user = Users.objects.get(id=self.user2.id)
        self.assertIn(user.last_name, 'updatedname',
                      'Updated name not found after update.')

    # Check user can view their own profile
    def test_view_own_profile(self):
        """Test viewing own profile"""
        response = self.client.get(reverse('users:user-profile'))
        # Verify rendered data
        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.last_name)
        self.assertContains(response, self.user.email)

    # Check a user can change their password
    def test_change_own_password(self):
        """Test changing own password"""
        # Set new password
        new_password = 'UpdatedPass1!'
        data = {
            'first_name': 'active',
            'last_name': 'staffuser',
            'email': 'staffuser@example.com',
            'password1': new_password,
            'password2': new_password
        }

        # Change password
        response = self.client.post(reverse('users:user-profile'), data)
        self.assertEqual(response.status_code, 302)

        # Refresh user from db
        self.user.refresh_from_db()

        # Check users password
        self.assertTrue(self.user.check_password(new_password),
                        'Password was not updated.')

        # Logout out of current session
        self.client.logout()

        # Login with new password
        do_login = self.client.login(email='staffuser@example.com',
                                     password='UpdatedPass1!')
        self.assertTrue(do_login, 'Login was not successful.')

        # Confirm logged by getting users profile and checking session
        response = self.client.get(reverse('users:user-profile'))
        user = response.wsgi_request.user  # Get authenticated user instance
        self.assertTrue(user.is_authenticated, 'User is not authenticated.')
        self.assertEqual(user.email, 'staffuser@example.com',
                         'Authenticated user does not match excpected email.')
        self.assertContains(response, user)  # Check user's profile is shown
