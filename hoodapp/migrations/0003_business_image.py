# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-09 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_remove_business_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]