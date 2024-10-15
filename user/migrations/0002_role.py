# Generated by Django 5.1.2 on 2024-10-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('display_name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('permissions', models.ManyToManyField(related_name='roles', to='user.permission')),
            ],
        ),
    ]
