# Generated by Django 4.0.2 on 2024-06-15 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_alter_form_collect_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_location_name', models.CharField(blank=True, max_length=100, null=True)),
                ('home_latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('home_longtude', models.CharField(blank=True, max_length=50, null=True)),
                ('response', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_form_response', to='index.responses')),
            ],
        ),
    ]
