from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        if not email:
            raise ValueError('A valid email address is required')
        if not password:
            raise ValueError('A password is required')
        email = self.normalize_email(email)
        user_name = email.split('@')[0]
        user = self.model(email=email, user_name=user_name, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, first_name, last_name, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    ROLE_TYPES = {
        "Staff": "Staff",
        "Client": "Client",
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

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.invoice_number} {self.client}" 

    def __str__(self):
        return self.user_name
