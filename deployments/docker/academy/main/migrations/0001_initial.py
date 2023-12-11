# Generated by Django 3.0.7 on 2023-12-11 20:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubActivitys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=20)),
                ('github_name', models.CharField(max_length=20)),
                ('repo_name', models.CharField(max_length=20)),
                ('activity_description', models.CharField(max_length=50)),
                ('evnet_content', models.TextField(blank=True, max_length=15750, validators=[django.core.validators.MaxLengthValidator(15750)])),
                ('created_date', models.DateTimeField(blank=True, help_text='HH:MM:SS DD Mmm YY, YYYY PST', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JsonStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('data', jsonfield.fields.JSONField(null=True)),
                ('created_date', models.DateTimeField(blank=True, help_text='HH:MM:SS DD Mmm YY, YYYY CDT', null=True)),
                ('updated_date', models.DateTimeField(blank=True, help_text='HH:MM:SS DD Mmm YY, YYYY CDT', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecureShell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='last update')),
                ('owner', models.CharField(max_length=60, null=True)),
                ('private_key', models.CharField(max_length=16384, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, null=True)),
                ('last_name', models.CharField(max_length=60, null=True)),
                ('email', models.EmailField(max_length=120, null=True)),
                ('subject', models.CharField(max_length=120, null=True)),
                ('body', models.CharField(max_length=750, null=True)),
                ('answer', models.TextField(blank=True, max_length=750, validators=[django.core.validators.MaxLengthValidator(750)])),
                ('publish', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_type', models.CharField(default='Basic', max_length=60)),
                ('payment_confirmation', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='last update')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
