# Generated by Django 5.0.4 on 2024-05-24 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cases',
            options={'permissions': [('can_view_cases', 'View Case'), ('can_edit_cases', 'Edit Case')], 'verbose_name': 'Cases', 'verbose_name_plural': 'Cases'},
        ),
    ]