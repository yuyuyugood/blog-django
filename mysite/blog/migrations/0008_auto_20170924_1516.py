# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170924_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='jpg',
            field=models.ImageField(upload_to='mysite/blog/media'),
        ),
    ]
