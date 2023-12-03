# Generated by Django 3.0.7 on 2022-07-03 03:41

from django.db import migrations, models
import django.core.validators
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20220517_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='zip_code',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=120, null=True),
        ),
    ]
