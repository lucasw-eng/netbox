# Generated by Django 3.2b1 on 2021-02-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0011_standardize_name_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tenantgroup',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
