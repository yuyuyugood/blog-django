# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='readcount',
            new_name='artid',
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_content',
        ),
        migrations.AddField(
            model_name='article',
            name='jianjie',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='jpg',
            field=models.FileField(default=0, upload_to=b''),
            preserve_default=False,
        ),
    ]
