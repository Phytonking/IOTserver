# Generated by Django 4.0.1 on 2022-02-19 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_u_account_user_serial_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='u',
            name='logged_in',
            field=models.BooleanField(null=True),
        ),
    ]
