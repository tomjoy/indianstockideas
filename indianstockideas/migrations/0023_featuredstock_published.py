# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-02 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0022_auto_20170702_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredstock',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]