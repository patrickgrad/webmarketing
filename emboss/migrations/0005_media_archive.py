# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emboss', '0004_media_parent_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='archive',
            field=models.BooleanField(default=0),
        ),
    ]
