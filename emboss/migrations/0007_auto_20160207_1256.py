# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-07 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('emboss', '0006_auto_20160207_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='embossdata',
            name='daily_agg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='utils.DataStream'),
        ),
        migrations.AddField(
            model_name='embossdata',
            name='monthly_agg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='utils.DataStream'),
        ),
        migrations.AddField(
            model_name='embossdata',
            name='monthly_agg_daily',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='utils.DataStream'),
        ),
        migrations.AddField(
            model_name='embossdata',
            name='monthly_agg_weekly',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='utils.DataStream'),
        ),
        migrations.AddField(
            model_name='embossdata',
            name='weekly_agg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='utils.DataStream'),
        ),
        migrations.AddField(
            model_name='embossdata',
            name='weekly_agg_daily',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='utils.DataStream'),
        ),
        migrations.AddField(
            model_name='embossdata',
            name='yearly_agg_monthly',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='utils.DataStream'),
        ),
        migrations.AddField(
            model_name='embossdata',
            name='yearly_agg_weekly',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='utils.DataStream'),
        ),
    ]
