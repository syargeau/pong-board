# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2023-12-12 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0016_auto_20231212_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='rating',
            field=models.IntegerField(blank=True, default=1450, null=True),
        ),
    ]