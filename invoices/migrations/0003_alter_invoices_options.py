# Generated by Django 5.0.4 on 2024-05-24 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_alter_invoices_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoices',
            options={'permissions': [('manage_invoices', 'Manage Invoices')], 'verbose_name': 'Invoices', 'verbose_name_plural': 'Invoices'},
        ),
    ]
