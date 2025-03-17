# Generated by Django 4.2.5 on 2024-11-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0009_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='carssell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.IntegerField()),
                ('model', models.CharField(max_length=50)),
                ('variant', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('fuel', models.CharField(max_length=50)),
                ('transmission', models.CharField(max_length=50)),
                ('km', models.IntegerField()),
                ('owners', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
