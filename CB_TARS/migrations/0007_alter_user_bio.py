# Generated by Django 4.2.16 on 2024-10-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0006_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
