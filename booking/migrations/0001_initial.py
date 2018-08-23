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
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(blank=True, max_length=25)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='landing.Stylist')),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stylist', to='landing.Stylist')),
            ],
        ),
    ]
