# Generated by Django 5.1.2 on 2024-10-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scms', '0005_content_delete_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='link_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]