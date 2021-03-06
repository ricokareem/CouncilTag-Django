# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-08 06:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('ingest', '0013_change_message_keytype'), ('ingest', '0014_change_message_keytype'), ('ingest', '0015_change_message_keytype'), ('ingest', '0016_change_message_keytype')]

    dependencies = [
        ('ingest', '0012_add_committee_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='agenda_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ingest.AgendaItem'),
        ),
        migrations.AlterField(
            model_name='message',
            name='committee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ingest.Committee'),
        ),
    ]
