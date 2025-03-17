# Generated by Django 4.2.5 on 2025-01-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0034_approvedcarbuyers'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsell',
            name='soldoutstatus',
            field=models.CharField(blank=True, choices=[('AVAILABLE', 'available'), ('UNAVAILABLE', 'unavailable'), ('SOLDOUT', 'soldout')], default='available', max_length=11, null=True),
        ),
    ]
