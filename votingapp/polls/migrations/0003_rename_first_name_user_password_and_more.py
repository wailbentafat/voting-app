# Generated by Django 5.0.7 on 2024-07-22 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_event_candidate_event_candidates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]