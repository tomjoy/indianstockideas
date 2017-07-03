# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-02 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0018_moneycontrolmapping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indianstockideasaction',
            name='action',
            field=models.CharField(choices=[('Run NSE', 'Run NSE'), ('Run Screener', 'Run Screener'), ('Fetch Data', 'Fetch Data'), ('Run MoneyControl', 'Run MoneyControl'), ('Run MoneyControl MutualFund', 'Run MoneyControl MutualFund')], default='Run NSE', max_length=50),
        ),
        migrations.AlterField(
            model_name='moneycontrolmapping',
            name='stockname',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='moneycontrolmapping',
            name='stockurl',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]