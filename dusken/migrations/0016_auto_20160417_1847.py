# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dusken', '0015_orgunit_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membercard',
            name='card_number',
            field=models.IntegerField(unique=True),
        ),
    ]
