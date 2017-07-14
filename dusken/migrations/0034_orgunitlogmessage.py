# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 15:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dusken', '0033_auto_20170709_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgUnitLogMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=500)),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='org_unit_changes', to=settings.AUTH_USER_MODEL)),
                ('org_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_messages', to='dusken.OrgUnit')),
            ],
            options={
                'verbose_name_plural': 'Org unit log messages',
                'verbose_name': 'Org unit log message',
            },
        ),
    ]