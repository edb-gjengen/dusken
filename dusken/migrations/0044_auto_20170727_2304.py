# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dusken', '0043_auto_20170727_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprofile',
            name='type',
            field=models.CharField(blank=True, choices=[('volunteers', 'Volunteers'), ('', 'Standard')], default='', max_length=255),
        ),
    ]
