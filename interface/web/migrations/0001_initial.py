# Generated by Django 4.0.1 on 2022-11-21 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='u',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('username', models.TextField(null=True)),
                ('password', models.TextField(null=True)),
                ('account_user_serial_key', models.TextField(null=True)),
                ('account_server_origin', models.TextField()),
                ('logged_in', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.TextField()),
                ('logged_out', models.BooleanField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='logged', to='web.u')),
            ],
        ),
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.TextField()),
                ('device_name', models.TextField()),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='linked_account', to='web.u')),
            ],
        ),
    ]
