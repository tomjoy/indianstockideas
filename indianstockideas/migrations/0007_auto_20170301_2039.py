# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0006_auto_20170301_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indianstockideasaction',
            name='executed_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
