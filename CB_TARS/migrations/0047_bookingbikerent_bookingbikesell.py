# Generated by Django 5.1.4 on 2025-02-16 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0046_car_renting_transactions_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingBikeRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('totalprice', models.IntegerField(blank=True, default=0, null=True)),
                ('approval_status', models.CharField(blank=True, default='pending', max_length=20, null=True)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CB_TARS.carrent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CB_TARS.user')),
            ],
        ),
        migrations.CreateModel(
            name='BookingBikesell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('approval_status', models.CharField(blank=True, default='pending', max_length=20, null=True)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CB_TARS.bikesell')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CB_TARS.user')),
            ],
        ),
    ]
