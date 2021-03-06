# Generated by Django 3.0.8 on 2021-11-02 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('user_id', models.CharField(default=True, max_length=275, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=64, null=True)),
                ('last_name', models.CharField(max_length=64, null=True)),
                ('user_email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('connection_id', models.CharField(max_length=128, null=True)),
                ('Premium_member', models.BooleanField(null=True)),
                ('Premium_member_rank', models.IntegerField(null=True)),
                ('Premium_membership_signup', models.DateTimeField(null=True)),
                ('Premium_membership_expiry', models.DateTimeField(null=True)),
                ('logged_in', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.UUIDField(null=True)),
                ('device_name', models.TextField(null=True)),
                ('registered', models.BooleanField(null=True)),
                ('created', models.DateTimeField(null=True)),
                ('IP_address', models.GenericIPAddressField(null=True)),
                ('registered_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_user', to='web.account')),
            ],
        ),
        migrations.CreateModel(
            name='action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('prev_device_status', models.TextField()),
                ('now_device_status', models.TextField()),
                ('client_ip_address', models.GenericIPAddressField()),
                ('acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_starter', to='web.account')),
                ('device_used', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signal_reciver', to='web.device')),
            ],
        ),
    ]
