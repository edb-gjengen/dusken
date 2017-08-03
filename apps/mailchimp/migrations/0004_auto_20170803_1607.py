# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailchimp', '0003_auto_20170801_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailchimpsubscription',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='mailchimpsubscription',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
