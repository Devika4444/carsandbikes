# Generated by Django 4.2.5 on 2024-12-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0017_alter_carsell_description_alter_carsell_owners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsell',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carsell',
            name='variant',
            field=models.CharField(max_length=50),
        ),
    ]
