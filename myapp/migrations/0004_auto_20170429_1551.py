# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170429_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smsphonemessagerecords',
            old_name='senderid',
            new_name='sender',
        ),
        migrations.RenameField(
            model_name='smsserviceaudit',
            old_name='senderid',
            new_name='sender',
        ),
        migrations.AlterField(
            model_name='smsphonemessagerecords',
            name='message',
            field=models.TextField(max_length=50),
        ),
    ]
