# Generated by Django 5.1.6 on 2025-03-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0065_alter_carrent_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spare',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
