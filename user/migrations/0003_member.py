# Generated by Django 5.1.2 on 2024-10-15 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=15)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('whatsapp', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=255)),
                ('confirm_password', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.role')),
            ],
        ),
    ]
