# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-15 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emboss', '0002_invoice_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='name',
            field=models.CharField(default='Untitled', max_length=50),
        ),
    ]