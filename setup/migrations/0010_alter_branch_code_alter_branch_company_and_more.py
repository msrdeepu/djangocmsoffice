# Generated by Django 5.1.2 on 2024-10-15 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0009_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(limit_choices_to={'active': 'yes'}, on_delete=django.db.models.deletion.CASCADE, to='setup.company'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branch',
            name='mobile',
            field=models.CharField(default='null', max_length=15),
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branch',
            name='phone',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=100)),
                ('opening_balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('bank_name', models.CharField(max_length=255)),
                ('bank_contact_number', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('bank_address', models.TextField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.branch')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.company')),
            ],
        ),
    ]
