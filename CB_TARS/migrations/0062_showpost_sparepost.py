# Generated by Django 5.1.2 on 2025-03-02 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0061_workpost_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='showpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('show', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CB_TARS.show')),
            ],
        ),
        migrations.CreateModel(
            name='sparepost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('spare', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CB_TARS.spare')),
            ],
        ),
    ]
