# Generated by Django 4.2.5 on 2025-01-25 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0035_carsell_soldoutstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingcarsell',
            name='approval_status',
            field=models.CharField(blank=True, default='pending', max_length=20, null=True),
        ),
    ]
