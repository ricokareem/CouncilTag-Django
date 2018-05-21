# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-11 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0013_change_message_keytype_squashed_0016_change_message_keytype'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='pro',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]