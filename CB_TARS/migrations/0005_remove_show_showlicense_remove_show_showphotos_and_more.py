# Generated by Django 5.0.2 on 2024-09-20 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0004_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='showlicense',
        ),
        migrations.RemoveField(
            model_name='show',
            name='showphotos',
        ),
        migrations.RemoveField(
            model_name='work',
            name='worklicense',
        ),
        migrations.RemoveField(
            model_name='work',
            name='workphotos',
        ),
    ]
