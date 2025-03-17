# Generated by Django 4.2.5 on 2024-11-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0010_carssell'),
    ]

    operations = [
        migrations.CreateModel(
            name='bikesell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.IntegerField()),
                ('year', models.IntegerField()),
                ('fuel', models.CharField(max_length=50)),
                ('km', models.IntegerField()),
                ('owners', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RenameModel(
            old_name='carssell',
            new_name='carsell',
        ),
    ]
