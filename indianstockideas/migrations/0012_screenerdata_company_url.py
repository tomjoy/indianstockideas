# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0011_featuredstock_ctolow'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenerdata',
            name='company_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
