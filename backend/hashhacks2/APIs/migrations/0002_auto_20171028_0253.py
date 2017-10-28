# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-28 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='Education',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='Property_Area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='daily_sms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='facebook_twitter',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='late_bill_days_avg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='network_bytes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='pan',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='postpaid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='similar_locations',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='usage_hours_per_week',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]