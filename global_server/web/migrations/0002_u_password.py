# Generated by Django 4.0.1 on 2022-02-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='u',
            name='password',
            field=models.TextField(null=True),
        ),
    ]
