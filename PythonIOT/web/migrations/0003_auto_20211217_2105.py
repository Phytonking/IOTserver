# Generated by Django 3.0.8 on 2021-12-17 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_account_password_hash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='acc',
        ),
        migrations.RemoveField(
            model_name='device',
            name='created',
        ),
        migrations.RemoveField(
            model_name='device',
            name='registered',
        ),
        migrations.RemoveField(
            model_name='device',
            name='registered_owner',
        ),
        migrations.DeleteModel(
            name='account',
        ),
    ]
