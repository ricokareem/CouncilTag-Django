# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-14 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0014_change_message_add_pro'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendaitem',
            name='agenda_item_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='agendaitem',
            name='meeting_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
