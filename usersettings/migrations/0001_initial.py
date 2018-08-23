# Generated by Django 2.1 on 2018-08-23 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('landing', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifications', models.BooleanField()),
                ('push_notifications', models.BooleanField()),
                ('text_notifications', models.BooleanField()),
                ('promotions', models.BooleanField()),
                ('search_engine', models.BooleanField()),
                ('deactivate', models.BooleanField()),
                ('time_zone', models.CharField(max_length=15)),
                ('languages', models.CharField(max_length=15)),
                ('currency', models.CharField(max_length=15)),
                ('account_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings_account', to='landing.Stylist')),
            ],
        ),
    ]