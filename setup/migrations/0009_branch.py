# Generated by Django 5.1.2 on 2024-10-15 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0008_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('active', models.BooleanField(default=True)),
                ('address', models.TextField()),
                ('company', models.ForeignKey(limit_choices_to={'status': 'active'}, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='setup.company')),
            ],
        ),
    ]
