# Generated by Django 5.0.4 on 2024-06-08 07:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_alter_clients_client_reference'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='portal_account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='client', to=settings.AUTH_USER_MODEL),
        ),
    ]