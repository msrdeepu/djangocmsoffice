# Generated by Django 5.1.2 on 2024-10-16 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scms', '0008_content_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='enable_gallery',
        ),
        migrations.RemoveField(
            model_name='content',
            name='enable_uploads',
        ),
    ]