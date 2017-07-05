# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-05 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0024_publisheddata'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredstock',
            name='bought',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='featuredstock',
            name='sold',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='mutualfundholding',
            name='bought',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='mutualfundholding',
            name='sold',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
