# Generated by Django 4.0.2 on 2024-06-15 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_homelocation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homelocation',
            old_name='event_location_name',
            new_name='home_location_name',
        ),
    ]
