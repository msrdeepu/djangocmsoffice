# Generated by Django 5.1.2 on 2024-10-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('partner', 'Partner'), ('agent', 'Agent'), ('client', 'Client')], max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=15)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('whatsapp', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
