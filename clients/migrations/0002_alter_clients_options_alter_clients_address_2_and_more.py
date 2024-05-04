# Generated by Django 5.0.4 on 2024-05-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Clients', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterField(
            model_name='clients',
            name='address_2',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='clients',
            name='address_3',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='clients',
            name='building_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='clients',
            name='city',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.EmailField(blank=True, max_length=124),
        ),
        migrations.AlterField(
            model_name='clients',
            name='first_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='clients',
            name='last_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='clients',
            name='middle_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='clients',
            name='mobile',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clients',
            name='post_code',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='clients',
            name='street',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]