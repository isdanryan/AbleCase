# Generated by Django 5.0.4 on 2024-07-16 09:14

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=64)),
                ('first_name', models.CharField(blank=True, max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=64)),
                ('middle_name', models.CharField(blank=True, max_length=64)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=124)),
                ('type', models.CharField(choices=[('Buisness', 'Buisness'), ('Individual', 'Individual')], default='Business', max_length=10)),
                ('building_number', models.CharField(blank=True, max_length=20)),
                ('street', models.CharField(blank=True, max_length=64)),
                ('address_2', models.CharField(blank=True, max_length=64)),
                ('address_3', models.CharField(blank=True, max_length=64)),
                ('city', models.CharField(blank=True, max_length=64)),
                ('post_code', models.CharField(blank=True, max_length=64)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=30)),
                ('has_portal_access', models.BooleanField(default=False)),
                ('client_reference', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'verbose_name': 'Clients',
                'verbose_name_plural': 'Clients',
                'permissions': [('can_view_clients', 'View Clients'), ('can_edit_clients', 'Edit Clients')],
            },
        ),
    ]
