# Generated by Django 5.1.2 on 2024-10-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scms', '0006_content_link_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='call_to_action_text',
            new_name='cta_action_text',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='call_to_action_body',
            new_name='cta_body',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='call_to_action_url',
            new_name='cta_link_url',
        ),
        migrations.RemoveField(
            model_name='content',
            name='call_to_action_header',
        ),
        migrations.AddField(
            model_name='content',
            name='cta_header',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]