# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0014_auto_20170402_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='indianstockideasaction',
            name='status',
            field=models.CharField(blank=True, default='Success', max_length=100, null=True),
        ),
    ]
