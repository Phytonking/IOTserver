# Generated by Django 4.0.1 on 2022-02-17 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0003_u_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.TextField()),
                ('file_size_bytes', models.BigIntegerField()),
                ('in_folder', models.TextField(null=True)),
                ('file_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='web.u')),
            ],
        ),
    ]