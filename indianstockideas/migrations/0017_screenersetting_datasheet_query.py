# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0016_nsesetting_formula'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenersetting',
            name='datasheet_query',
            field=models.TextField(default='salesFlag = sales[0]<sales[1]<sales[2]<sales[3]<sales[4];profitFlag = netProfit[0]<netProfit[1]<netProfit[2]<netProfit[3]<netProfit[4];featured = salesFlag and profitFlag and salesCurrentQuarter>salesPreviousQuarter and netProfitCurrentQuarter>netProfitPreviousQuarter;', max_length=500),
        ),
    ]
