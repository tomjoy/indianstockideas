# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0008_nsesetting_date6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nsesetting',
            name='date6',
            field=models.DateField(verbose_name='NSE Date6'),
        ),
    ]
