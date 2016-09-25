# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 23:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dusken', '0022_auto_20160925_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('price_nok', models.IntegerField(help_text='In øre')),
                ('payment_method', models.CharField(choices=[('app', 'Mobile app'), ('sms', 'SMS'), ('card', 'Credit card'), ('other', 'Other')], default='other', max_length=254)),
                ('transaction_id', models.CharField(blank=True, help_text='Stripe charge ID, Kassa event ID, SMS event ID or App event ID', max_length=254, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='membership',
            name='payment',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dusken.Membership'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
