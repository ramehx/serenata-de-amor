# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_create_model_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='status',
            field=models.DecimalField(db_index=True, decimal_places=0, max_digits=25, verbose_name='Tweet ID'),
        ),
    ]
