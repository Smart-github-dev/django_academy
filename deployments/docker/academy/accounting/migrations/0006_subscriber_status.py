# Generated by Django 3.0.7 on 2023-11-19 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0005_auto_20220702_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('canceled', 'Canceled'), ('new', 'New')], default='new', max_length=10),
        ),
    ]
