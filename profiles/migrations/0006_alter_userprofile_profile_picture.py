# Generated by Django 5.1.6 on 2025-02-16 21:12

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_remove_userprofile_age_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='nobody_nrbk5n', max_length=255, null=True, verbose_name='image'),
        ),
    ]
