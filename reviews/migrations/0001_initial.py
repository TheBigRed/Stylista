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
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed_client', models.BooleanField(blank=True, default=None)),
                ('title', models.CharField(blank=True, max_length=25)),
                ('review', models.TextField(blank=True)),
                ('rating', models.FloatField(blank=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('helpful_count', models.IntegerField(blank=True, default=0)),
                ('unhelpful_count', models.IntegerField(blank=True, default=0)),
                ('helpful_total_count', models.IntegerField(blank=True, default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_review', to='landing.Stylist')),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stylist_review', to='landing.Stylist')),
            ],
        ),
    ]
