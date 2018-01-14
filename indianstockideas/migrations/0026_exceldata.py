# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-30 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indianstockideas', '0025_auto_20170705_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stock_Name', models.CharField(blank=True, max_length=150, null=True)),
                ('Sector', models.CharField(blank=True, max_length=150, null=True)),
                ('Last_Price', models.CharField(blank=True, max_length=150, null=True)),
                ('Capital', models.CharField(blank=True, max_length=150, null=True)),
                ('Date1', models.CharField(blank=True, max_length=150, null=True)),
                ('Date2', models.CharField(blank=True, max_length=150, null=True)),
                ('Date3', models.CharField(blank=True, max_length=150, null=True)),
                ('Date4', models.CharField(blank=True, max_length=150, null=True)),
                ('Date5', models.CharField(blank=True, max_length=150, null=True)),
                ('Date6', models.CharField(blank=True, max_length=150, null=True)),
                ('Result_Date', models.CharField(blank=True, max_length=150, null=True)),
                ('PAT_Quarter_P1', models.CharField(blank=True, max_length=150, null=True)),
                ('PAT_Quarter_P2', models.CharField(blank=True, max_length=150, null=True)),
                ('PAT_Quarter_P3', models.CharField(blank=True, max_length=150, null=True)),
                ('PAT_Quarter_P4', models.CharField(blank=True, max_length=150, null=True)),
                ('PAT_Quarter_Current', models.CharField(blank=True, max_length=150, null=True)),
                ('PAT_Annual_P1', models.CharField(blank=True, max_length=150, null=True)),
                ('PAT_Annual_P2', models.CharField(blank=True, max_length=150, null=True)),
                ('PAT_Annual_P3', models.CharField(blank=True, max_length=150, null=True)),
                ('PAT_Annual_P4', models.CharField(blank=True, max_length=150, null=True)),
                ('PAT_Annual_Current', models.CharField(blank=True, max_length=150, null=True)),
                ('PBT_Quarter_P1', models.CharField(blank=True, max_length=150, null=True)),
                ('PBT_Quarter_P2', models.CharField(blank=True, max_length=150, null=True)),
                ('PBT_Quarter_P3', models.CharField(blank=True, max_length=150, null=True)),
                ('PBT_Quarter_P4', models.CharField(blank=True, max_length=150, null=True)),
                ('PBT_Quarter_Current', models.CharField(blank=True, max_length=150, null=True)),
                ('PBT_Annual_P1', models.CharField(blank=True, max_length=150, null=True)),
                ('PBT_Annual_P2', models.CharField(blank=True, max_length=150, null=True)),
                ('PBT_Annual_P3', models.CharField(blank=True, max_length=150, null=True)),
                ('PBT_Annual_P4', models.CharField(blank=True, max_length=150, null=True)),
                ('PBT_Annual_Current', models.CharField(blank=True, max_length=150, null=True)),
                ('Sales_Quarter_P1', models.CharField(blank=True, max_length=150, null=True)),
                ('Sales_Quarter_P2', models.CharField(blank=True, max_length=150, null=True)),
                ('Sales_Quarter_P3', models.CharField(blank=True, max_length=150, null=True)),
                ('Sales_Quarter_P4', models.CharField(blank=True, max_length=150, null=True)),
                ('Sales_Quarter_Current', models.CharField(blank=True, max_length=150, null=True)),
                ('Sales_Annual_P1', models.CharField(blank=True, max_length=150, null=True)),
                ('Sales_Annual_P2', models.CharField(blank=True, max_length=150, null=True)),
                ('Sales_Annual_P3', models.CharField(blank=True, max_length=150, null=True)),
                ('Sales_Annual_P4', models.CharField(blank=True, max_length=150, null=True)),
                ('Sales_Annual_Current', models.CharField(blank=True, max_length=150, null=True)),
                ('Exception_and_extra_ordinary_items_Annual_P1', models.CharField(blank=True, max_length=150, null=True)),
                ('Exception_and_extra_ordinary_items_Annual_P2', models.CharField(blank=True, max_length=150, null=True)),
                ('Exception_and_extra_ordinary_items_Annual_P3', models.CharField(blank=True, max_length=150, null=True)),
                ('Exception_and_extra_ordinary_items_Annual_P4', models.CharField(blank=True, max_length=150, null=True)),
                ('Exception_and_extra_ordinary_items_Annual_Current', models.CharField(blank=True, max_length=150, null=True)),
                ('Interest_Annual_P1', models.CharField(blank=True, max_length=150, null=True)),
                ('Interest_Annual_P2', models.CharField(blank=True, max_length=150, null=True)),
                ('Interest_Annual_P3', models.CharField(blank=True, max_length=150, null=True)),
                ('Interest_Annual_P4', models.CharField(blank=True, max_length=150, null=True)),
                ('Interest_Annual_Current', models.CharField(blank=True, max_length=150, null=True)),
                ('EPS_Annual_P1', models.CharField(blank=True, max_length=150, null=True)),
                ('EPS_Annual_P2', models.CharField(blank=True, max_length=150, null=True)),
                ('EPS_Annual_P3', models.CharField(blank=True, max_length=150, null=True)),
                ('EPS_Annual_P4', models.CharField(blank=True, max_length=150, null=True)),
                ('EPS_Annual_Current', models.CharField(blank=True, max_length=150, null=True)),
                ('Mutual_Fund_previous', models.CharField(blank=True, max_length=150, null=True)),
                ('Mutual_Fund_current', models.CharField(blank=True, max_length=150, null=True)),
                ('Market_Cap', models.CharField(blank=True, max_length=150, null=True)),
                ('Book_Value', models.CharField(blank=True, max_length=150, null=True)),
                ('Face_Value', models.CharField(blank=True, max_length=150, null=True)),
                ('PE', models.CharField(blank=True, max_length=150, null=True)),
                ('DE_Ratio', models.CharField(blank=True, max_length=150, null=True)),
                ('Pledge', models.CharField(blank=True, max_length=150, null=True)),
                ('Divident_Ratio', models.CharField(blank=True, max_length=150, null=True)),
                ('Promoters_Holding_Last', models.CharField(blank=True, max_length=150, null=True)),
                ('Promoters_Holding_Current', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]