# Generated by Django 5.0.4 on 2024-05-24 17:26

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0003_alter_users_options_alter_users_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('permission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.permission')),
            ],
            options={
                'permissions': [('has_invoices', 'Manage Invoices'), ('has_users', 'Manage Users'), ('has_view_cases', 'View Cases'), ('has_edit_cases', 'Manage Case'), ('has_view_clients', 'View Clients'), ('has_edit_clients', 'Manage Clients'), ('has_online_portal', 'Online Portal')],
            },
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('Staff', 'Staff'), ('Client', 'Client'), ('Admin', 'Admin')], max_length=50),
        ),
    ]
