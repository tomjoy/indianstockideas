from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Registration(models.Model):
    first_name = models.CharField(max_length=200,default = "")
    last_name = models.CharField(max_length=200,default = "")
    email = models.EmailField(max_length=300,default = "")
    phone = models.PositiveIntegerField(default = "1")
    date = models.DateField('Date of ride',blank = True,null = True)
    time = models.CharField(max_length=200)
    
    
    
class ScreenerSetting(models.Model):
    name = models.CharField(max_length=200,default = "screener")
    login_username = models.CharField(max_length=200,default = "gittopaul2@gmail.com")
    login_password = models.CharField(max_length=200,default = "a12345")
    login_url = models.URLField(default='https://www.screener.in/login/')
    api_url = models.URLField(default='https://www.screener.in/api/screens/query/?query=')
    query = models.TextField(max_length=500,default = "Current+ratio+%3E+1.2+AND%0D%0AEPS+%3E+EPS+last+year+AND%0D%0ASales+last+year+%3E+Sales+preceding+year+AND%0D%0ANet+Profit+last+year+%3E+Net+Profit+preceding+year+AND%0D%0AMarket+Capitalization+%3E+5+AND%0D%0ANet+Profit++%3E+10+AND%0D%0ANet+Profit+last+year+%3E+5+AND%0D%0Acurrenttohigh+%3C+81")
    active = models.BooleanField(default = False)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    
class NSESetting(models.Model):
    name = models.CharField(max_length=100,default = "nse")
    date1 = models.DateField('NSE Date1',)
    date2 = models.DateField('NSE Date2')
    date3 = models.DateField('NSE Date3')
    date4 = models.DateField('NSE Date4')
    date5 = models.DateField('NSE Date5')
    date6 = models.DateField('NSE Date6')
    nse_url = models.URLField(default='https://www.nseindia.com/content/historical/EQUITIES/')
    formula = models.TextField(max_length=500,default ="f1 = (dc1*1.2)<(dc2);f2 = (dc1*1.2)<(dc3);f3 = (dc1*1.2)<(dc4);f4 = (dc4*0.8)>(dc5);f5 = (dc4*0.9)>(dc6);f6 = (dc1*0.51)<(dc6);formula = f1 and f2 and f3 and f4 and f5 and f6")
    active = models.BooleanField(default = False)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class IndianStockIdeasAction(models.Model):
    CHOICES = (
        ('Run NSE', 'Run NSE'),
        ('Run Screener', 'Run Screener'),
        ('Fetch Data', 'Fetch Data'),
        ('Run MoneyControl', 'Run MoneyControl'),
    )
    
    action = models.CharField(max_length=50,choices = CHOICES, default = 'Run NSE')
    status = models.CharField(max_length=100,blank = True,null = True,default='Success')
    executed_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.action
    

class ScreenerData(models.Model):
    symbol = models.CharField(max_length=100,blank = True,null = True)
    current_price = models.CharField(max_length=100,blank = True,null = True)
    price_to_earning = models.CharField(max_length=100,blank = True,null = True)
    market_capitalization = models.CharField(max_length=100,blank = True,null = True)
    yoy_quarterly_profit_growth = models.CharField(max_length=100,blank = True,null = True)
    yoy_quarterly_sales_growth = models.CharField(max_length=100,blank = True,null = True)
    net_profit = models.CharField(max_length=100,blank = True,null = True)
    profit_growth_3years = models.CharField(max_length=100,blank = True,null = True)
    profit_growth_5years = models.CharField(max_length=100,blank = True,null = True)
    sales_growth_5years = models.CharField(max_length=100,blank = True,null = True)
    sales_growth_3years = models.CharField(max_length=100,blank = True,null = True)
    ctohigh = models.CharField(max_length=100,blank = True,null = True)
    ctolow = models.CharField(max_length=100,blank = True,null = True)
    ftw_index = models.CharField(max_length=100,blank = True,null = True)
    cash_from_operations_last_year = models.CharField(max_length=100,blank = True,null = True)
    cash_from_operations_preceding_year = models.CharField(max_length=100,blank = True,null = True)
    #company_url = models.CharField(max_length=150,blank = True,null = True)
    executed_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.symbol
    
class NseData(models.Model):
    symbol = models.CharField(max_length=100,blank = True,null = True)
    series = models.CharField(max_length=100,blank = True,null = True)
    open = models.CharField(max_length=100,blank = True,null = True)
    high = models.CharField(max_length=100,blank = True,null = True)
    low = models.CharField(max_length=100,blank = True,null = True)
    close = models.CharField(max_length=100,blank = True,null = True)
    last = models.CharField(max_length=100,blank = True,null = True)
    prevclose = models.CharField(max_length=100,blank = True,null = True)
    tottrdqty = models.CharField(max_length=100,blank = True,null = True)
    tottrdval = models.CharField(max_length=100,blank = True,null = True)
    timestamp = models.CharField(max_length=100,blank = True,null = True)
    totaltrades = models.CharField(max_length=100,blank = True,null = True)
    isin = models.CharField(max_length=100,blank = True,null = True)
    def __str__(self):
        return self.symbol
    
class FeaturedStock(models.Model):
    symbol = models.CharField(max_length=100,blank = True,null = True)
    series = models.CharField(max_length=100,blank = True,null = True)
    open = models.CharField(max_length=100,blank = True,null = True)
    high = models.CharField(max_length=100,blank = True,null = True)
    low = models.CharField(max_length=100,blank = True,null = True)
    close = models.CharField(max_length=100,blank = True,null = True)
    last = models.CharField(max_length=100,blank = True,null = True)
    prevclose = models.CharField(max_length=100,blank = True,null = True)
    tottrdqty = models.CharField(max_length=100,blank = True,null = True)
    tottrdval = models.CharField(max_length=100,blank = True,null = True)
    timestamp = models.CharField(max_length=100,blank = True,null = True)
    totaltrades = models.CharField(max_length=100,blank = True,null = True)
    isin = models.CharField(max_length=100,blank = True,null = True)
    current_price = models.CharField(max_length=100,blank = True,null = True)
    price_to_earning = models.CharField(max_length=100,blank = True,null = True)
    market_capitalization = models.CharField(max_length=100,blank = True,null = True)
    yoy_quarterly_profit_growth = models.CharField(max_length=100,blank = True,null = True)
    yoy_quarterly_sales_growth = models.CharField(max_length=100,blank = True,null = True)
    net_profit = models.CharField(max_length=100,blank = True,null = True)
    profit_growth_3years = models.CharField(max_length=100,blank = True,null = True)
    profit_growth_5years = models.CharField(max_length=100,blank = True,null = True)
    sales_growth_5years = models.CharField(max_length=100,blank = True,null = True)
    sales_growth_3years = models.CharField(max_length=100,blank = True,null = True)
    ctohigh = models.CharField(max_length=100,blank = True,null = True)
    ctolow = models.CharField(max_length=100,blank = True,null = True)
    ftw_index = models.CharField(max_length=100,blank = True,null = True)
    cash_from_operations_last_year = models.CharField(max_length=100,blank = True,null = True)
    cash_from_operations_preceding_year = models.CharField(max_length=100,blank = True,null = True)
    recommended = models.BooleanField(default = False)
    executed_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.symbol
    
