# Generated by Django 5.0.4 on 2024-05-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0009_alter_invoices_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='vat',
            field=models.CharField(choices=[('ZERO', 'ZERO'), ('10%', '10%'), ('15%', '15%'), ('20%', '20%')], default='20%', max_length=10),
        ),
    ]
