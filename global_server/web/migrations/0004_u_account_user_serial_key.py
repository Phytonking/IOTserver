# Generated by Django 4.0.1 on 2022-02-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_u_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='u',
            name='account_user_serial_key',
            field=models.TextField(null=True),
        ),
    ]
