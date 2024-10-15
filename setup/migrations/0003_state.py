# Generated by Django 5.1.2 on 2024-10-15 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0002_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('country', models.ForeignKey(limit_choices_to={'status': 'active'}, on_delete=django.db.models.deletion.CASCADE, to='setup.country')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
    ]