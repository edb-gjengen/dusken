# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import dusken.managers


class Migration(migrations.Migration):

    dependencies = [
        ('dusken', '0047_auto_20170803_1607'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='duskenuser',
            managers=[
                ('objects', dusken.managers.DuskenUserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='duskenuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=254, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='duskenuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=254, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('app', 'Mobile app'), ('sms', 'SMS'), ('card', 'Credit card'), ('cash_register', 'Cash register'), ('other', 'Other')], default='other', max_length=254),
        ),
    ]
