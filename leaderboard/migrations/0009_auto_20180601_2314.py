# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-01 23:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0008_match_datetime'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
