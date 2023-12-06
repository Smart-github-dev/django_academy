# Generated by Django 3.0.7 on 2023-12-06 18:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20231206_0700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='githubactivitys',
            old_name='commit_id',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='githubactivitys',
            old_name='distinct',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='githubactivitys',
            name='added',
        ),
        migrations.RemoveField(
            model_name='githubactivitys',
            name='author',
        ),
        migrations.RemoveField(
            model_name='githubactivitys',
            name='committer',
        ),
        migrations.RemoveField(
            model_name='githubactivitys',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='githubactivitys',
            name='message',
        ),
        migrations.RemoveField(
            model_name='githubactivitys',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='githubactivitys',
            name='removed',
        ),
        migrations.RemoveField(
            model_name='githubactivitys',
            name='tree_id',
        ),
        migrations.AddField(
            model_name='githubactivitys',
            name='evnet_content',
            field=models.TextField(blank=True, max_length=15750, validators=[django.core.validators.MaxLengthValidator(15750)]),
        ),
    ]
