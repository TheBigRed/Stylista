# Generated by Django 2.0.4 on 2018-05-30 05:33

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='stylist_type',
            field=models.CharField(blank=True, choices=[('BARBER', 'Barber'), ('HAIR_STYLIST', 'Hair Stylist'), ('MAKEUP', 'Makeup Artist'), ('MUAH', 'Make Up And Hair'), ('NAILS', 'Nail Technician'), ('CLIENT', 'Client')], max_length=25),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='picture',
            field=models.ImageField(default='/user/storefront/gallery.jpg', upload_to=core.models.Gallery.user_directory_path1),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Stylist'),
        ),
    ]