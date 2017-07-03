# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-02 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0023_featuredstock_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockname', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('executed_date', models.DateField(auto_now=True)),
            ],
        ),
    ]