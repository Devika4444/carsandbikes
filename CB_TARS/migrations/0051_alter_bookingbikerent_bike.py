# Generated by Django 5.1.4 on 2025-02-16 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0050_remove_bikerent_rentalperiod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingbikerent',
            name='bike',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CB_TARS.bikerent'),
        ),
    ]
