# Generated by Django 5.0.4 on 2024-05-09 13:38

import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0005_clients_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
                ('short_code', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'Case Types',
                'verbose_name_plural': 'Case Types',
            },
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.IntegerField()),
                ('case_name', models.CharField(blank=True, max_length=64)),
                ('address', models.TextField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('assigned', models.CharField(blank=True, max_length=64)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=10)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.clients')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cases.casetypes')),
            ],
            options={
                'verbose_name': 'Cases',
                'verbose_name_plural': 'Cases',
            },
        ),
    ]
