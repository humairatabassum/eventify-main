# Generated by Django 4.2.3 on 2023-09-17 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='event_location',
            new_name='event_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='date_of_event',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='event_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='event_type',
        ),
    ]
