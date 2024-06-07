# Generated by Django 5.0.4 on 2024-05-21 21:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('short_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField(verbose_name='Invoice No')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('term', models.CharField(choices=[('On Receipt', 'On Receipt'), ('7 Days', '7 days'), ('14 Days', '14 days'), ('30 Days', '30 days'), ('Custom', 'Custom')], default='On Reciept', max_length=64)),
                ('date_due', models.DateField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, default='0.00', max_digits=19)),
                ('vat', models.CharField(choices=[('ZERO', 'ZERO'), ('10%', '10%'), ('15%', '15%'), ('20%', '20%')], default='20%', max_length=10)),
                ('total_due', models.DecimalField(decimal_places=2, default='0.00', max_digits=19)),
                ('case_address', models.CharField(blank=True, max_length=256, null=True)),
                ('case_type', models.CharField(blank=True, max_length=64, null=True)),
                ('case_name', models.CharField(blank=True, max_length=64, null=True)),
                ('invoice_code', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Sent', 'Sent'), ('Not Sent', 'Not Sent')], default='Not Sent', max_length=64)),
                ('notes', models.TextField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.cases')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.clients')),
            ],
        ),
    ]
