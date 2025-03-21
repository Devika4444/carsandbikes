# Generated by Django 5.1.6 on 2025-02-26 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0057_bike_selling_transactions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookingworkshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('approval_status', models.CharField(blank=True, default='pending', max_length=20, null=True)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CB_TARS.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CB_TARS.user')),
            ],
        ),
    ]
