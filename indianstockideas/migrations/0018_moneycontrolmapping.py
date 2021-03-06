# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-02 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0017_screenersetting_datasheet_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyControlMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockname', models.CharField(blank=True, max_length=100, null=True)),
                ('sector', models.CharField(blank=True, max_length=100, null=True)),
                ('stockurl', models.CharField(blank=True, max_length=100, null=True)),
                ('urlsplit1', models.CharField(blank=True, max_length=100, null=True)),
                ('urlsplit2', models.CharField(blank=True, max_length=100, null=True)),
                ('urlsplit3', models.CharField(blank=True, max_length=100, null=True)),
                ('executed_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
