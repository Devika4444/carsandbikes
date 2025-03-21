# Generated by Django 4.2.5 on 2024-12-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_TARS', '0013_merge_0011_bikerent_carrent_0012_alter_carsell_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikerent',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bikesell',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carrent',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('approved', 'Approved'), ('reject', 'Reject')], default='applied', max_length=20),
        ),
        migrations.AddField(
            model_name='spare',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('approved', 'Approved'), ('reject', 'Reject')], default='applied', max_length=20),
        ),
        migrations.AddField(
            model_name='work',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('approved', 'Approved'), ('reject', 'Reject')], default='applied', max_length=20),
        ),
        migrations.AlterField(
            model_name='bikerent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bikesell',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='carrent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='carsell',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='show',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='spare',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='work',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
