from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        BaseUserManager)
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name,
                    password, **extra_fields):
        if not email:
            raise ValueError('A valid email address is required')
        if not password:
            raise ValueError('A password is required')
        email = self.normalize_email(email)
        user_name = email
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, last_name=last_name,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name,
                         password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, first_name, last_name,
                                password, **extra_fields)

    # Custom get_user_permissions method
    # required as using custom UserManager
    def get_user_permissions(self, user_object, obj=None):
        permissions = set()

        # Checks if the user has any of the permissions
        # then adds them to the permissions set
        # so they can be checked on the UserUpdate view
        if user_object.has_perm('clients.can_view_clients'):
            permissions.add('can_view_clients')
        if user_object.has_perm('clients.can_edit_clients'):
            permissions.add('can_view_clients')
        if user_object.has_perm('cases.can_view_cases'):
            permissions.add('can_view_cases')
        if user_object.has_perm('cases.can_edit_cases'):
            permissions.add('can_edit_cases')
        if user_object.has_perm('invoices.manage_invoices'):
            permissions.add('manage_invoices')
        if user_object.has_perm('users.manage_users'):
            permissions.add('manage_users')

        return permissions


class Users(AbstractBaseUser, PermissionsMixin):
    ROLE_TYPES = {
        "Staff": "Staff",
        "Client": "Client",
        "Admin": "Admin",
    }
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(max_length=50, choices=ROLE_TYPES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    # Required by the user manager method
    def get_user_permissions(self):
        return self.user_permissions.all()

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"

        permissions = [
            ("manage_users", "Manage Users",)
        ]

    def __str__(self):
        return self.email


class Tasks(models.Model):
    task = models.TextField(blank=False, null=False)
    due_date = models.DateField(default=timezone.now)
    user = models.ForeignKey("Users", on_delete=models.CASCADE)
