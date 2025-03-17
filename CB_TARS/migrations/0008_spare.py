# Generated by Django 4.2.5 on 2024-10-26 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0007_alter_user_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='spare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sparename', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
                ('spareaddress', models.CharField(max_length=100)),
                ('spareregno', models.CharField(max_length=50)),
            ],
        ),
    ]
