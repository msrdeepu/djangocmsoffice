# Generated by Django 5.1.2 on 2024-10-16 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scms', '0003_alter_settings_value'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Settings',
        ),
    ]