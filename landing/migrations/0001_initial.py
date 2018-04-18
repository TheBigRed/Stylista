# Generated by Django 2.0.4 on 2018-04-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('joined_date', models.DateTimeField(verbose_name='date joined')),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
