# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170924_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='jpg',
            field=models.FileField(upload_to='statics/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
