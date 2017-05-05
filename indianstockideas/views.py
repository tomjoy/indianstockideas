from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import logout
from models import Registration
from django.conf import settings
import json,requests
from lxml import html
from StringIO import StringIO
from zipfile import ZipFile
from .models import NSESetting,ScreenerSetting, ScreenerData, FeaturedStock, NseData, IndianStockIdeasAction
from lxml import etree
import urllib,xlrd
from multiprocessing import Process

class IndexView(generic.TemplateView):
    template_name = 'indianstockideas/index2.html'
    
       
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        commondata = FeaturedStock.objects.filter(recommended = True)
        #print downloadExcel('/company/SATIN/'),"flag"
        context.update({
	      'commondata':list(commondata.values_list()),   
	      'headers':['SYMBOL','SERIES','OPEN','HIGH','LOW','CLOSE','LAST','PREVCLOSE','TOTTRDQTY','TOTTRDVAL','TIMESTAMP','TOTALTRADES','ISIN', "Current price", "Price to Earning", "Market Capitalization", "YOY Quarterly profit growth", 
	    			"YOY Quarterly sales growth", "Net profit", "Profit growth 3Years", "Profit growth 5Years", "Sales growth 5Years",
	    			 "Sales growth 3Years", "ctohigh", "c2low", "52w Index", "Cash from operations last year", "Cash from operations preceding year","Featured", "Date"]           
	    })
        return context
    
class AllDataView(generic.TemplateView):
    template_name = 'indianstockideas/index2.html'
    
       
    def get_context_data(self, **kwargs):
        context = super(AllDataView, self).get_context_data(**kwargs)
        commondata = FeaturedStock.objects.all()
        #print downloadExcel('/company/SATIN/'),"flag"
        context.update({
          'commondata':list(commondata.values_list()),   
          'headers':['SYMBOL','SERIES','OPEN','HIGH','LOW','CLOSE','LAST','PREVCLOSE','TOTTRDQTY','TOTTRDVAL','TIMESTAMP','TOTALTRADES','ISIN', "Current price", "Price to Earning", "Market Capitalization", "YOY Quarterly profit growth", 
                    "YOY Quarterly sales growth", "Net profit", "Profit growth 3Years", "Profit growth 5Years", "Sales growth 5Years",
                     "Sales growth 3Years", "ctohigh", "c2low", "52w Index", "Cash from operations last year", "Cash from operations preceding year","Featured","Date"]           
        })
        return context
    
    
class AnalysisView(generic.TemplateView):
    template_name = 'indianstockideas/index2.html'
    
       
    def get_context_data(self, **kwargs):
        context = super(AnalysisView, self).get_context_data(**kwargs)
        commondata = FeaturedStock.objects.filter(recommended = True)
        analysisData = []
        for data in commondata:
            url = "https://www.screener.in/api/company/"
            resp = requests.get(url=url+data.symbol)
            jsonData = json.loads(resp.text)
            current_price = jsonData["warehouse_set"]["current_price"]
            percentage = ((float(current_price)-float(data.close))/float(data.close))*100
            analysis =  percentage>0
            analysisData.append(["",data.symbol,data.close,str(current_price),percentage, analysis])
            
        #print downloadExcel('/company/SATIN/'),"flag"
        context.update({
          'commondata':analysisData,   
          'headers':['SYMBOL','FEATURED PRICE',"CURRENT PRICE",'VARIATION %','ANALYSIS']})
        return context
    
class NseDataView(generic.TemplateView):
    template_name = 'indianstockideas/index2.html'
    
       
    def get_context_data(self, **kwargs):
        context = super(NseDataView, self).get_context_data(**kwargs)
        commondata = NseData.objects.all()
        #print downloadExcel('/company/SATIN/'),"flag"
        context.update({
          'commondata':list(commondata.values_list()),   
          'headers':['SYMBOL','SERIES','OPEN','HIGH','LOW','CLOSE','LAST','PREVCLOSE','TOTTRDQTY','TOTTRDVAL','TIMESTAMP','TOTALTRADES','ISIN' ]           
        })
        return context


class ScreenerView(generic.TemplateView):
    template_name = 'indianstockideas/index3.html'
    
       
    def get_context_data(self, **kwargs):
        context = super(ScreenerView, self).get_context_data(**kwargs)
        commondata = ScreenerData.objects.all()
        context.update({
          'commondata':list(commondata.values_list()),   
          'headers':['SYMBOL', "Current price", "Price to Earning", "Market Capitalization", "YOY Quarterly profit growth", 
                    "YOY Quarterly sales growth", "Net profit", "Profit growth 3Years", "Profit growth 5Years", "Sales growth 5Years",
                     "Sales growth 3Years", "ctohigh", "c2low", "52w Index", "Cash from operations last year", "Cash from operations preceding year","Date"]           
        })
        return context
    
# class HomeView(CreateView):
#     template_name = 'indianstockideas/home.html'
#     def dispatch(self, request, *args, **kwargs):
#         # check if there is some video onsite
#         
#         return HttpResponse(getscreener())
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def executescript(type):
    if type=='Run NSE':
        obj = NSESetting.objects.filter(active=True)[0]
        dates = {1:'date1',2:'date2',3:'date3',4:'date4',5:'date5',6:'date6'}
        import os
        filelist = [ f for f in os.listdir("csvfiles/")]
        for f in filelist:
            os.remove('csvfiles/'+f)
        for date in dates:
            date = getattr(obj, dates[date])
            nw = date.strftime('%d-%b-%Y').split('-')
            fname = 'cm'+nw[0]+nw[1].upper()+nw[2]+'bhav.csv'
            url = obj.nse_url+nw[2]+'/'+nw[1].upper()+'/'+fname+'.zip'
        #'2016/NOV/cm08NOV2016bhav.csv.zip
            
            s=requests.get(url,stream=True)
            v = ZipFile(StringIO(s.content))
            v.extractall('csvfiles/')
    elif type == "Run Screener":
        screens = getscreener()
        ScreenerData.objects.all().delete()
        for i,screencol in enumerate(screens):
                company = screencol[0].split('/')[2]
                obj = ScreenerData(
                                    symbol = company,
                                    current_price = screencol[2],
                                    price_to_earning = screencol[3],
                                    market_capitalization = screencol[4], 
                                    yoy_quarterly_profit_growth = screencol[5],
                                    yoy_quarterly_sales_growth = screencol[6],
                                    net_profit = screencol[7],
                                    profit_growth_3years = screencol[8],
                                    profit_growth_5years = screencol[9],
                                    sales_growth_5years = screencol[10],
                                    sales_growth_3years = screencol[11],
                                    ctohigh = screencol[12],
                                    ftw_index = screencol[13],
                                    cash_from_operations_last_year =screencol[14], 
                                    cash_from_operations_preceding_year = screencol[15])
                                    
                obj.save()
    elif type == "Fetch Data":
        obj = IndianStockIdeasAction.objects.get(action='Fetch Data')
        obj.status = "In Progress"
        obj.save()
        import thread
        thread.start_new_thread( fetchData,() )
        #p.join()
        
def fetchData():
    try:
        obj = NSESetting.objects.filter(active=True)[0]
        
        dates = {1:'date1',2:'date2',3:'date3',4:'date4',5:'date5',6:'date6'}
        import csv
        count = 0
        filedict={}
        NseData.objects.all().delete()
        FeaturedStock.objects.all().delete()
        for d in dates:
            date = getattr(obj, dates[d])
            nw = date.strftime('%d-%b-%Y').split('-')
            fname = 'cm'+nw[0]+nw[1].upper()+nw[2]+'bhav.csv'
            with open('csvfiles/'+fname, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                filedict[dates[d]] = []
                for i,row in enumerate(reader):
                    if i:
                        if row[1]=="EQ":
                            filedict[dates[d]].append(row[0:])
                    count =i
        finalList = []
        fstring = obj.formula
        obj = IndianStockIdeasAction.objects.get(action='Fetch Data')
        obj.status = "Formulating Nse Data"
        obj.save()
        for row in filedict['date6']:
            dc1 = findCompany(row[0],filedict['date1'])
            dc2 = findCompany(row[0],filedict['date2'])
            dc3 = findCompany(row[0],filedict['date3'])
            dc4 = findCompany(row[0],filedict['date4'])
            dc5 = findCompany(row[0],filedict['date5'])
            dc6 = row
            #(C13*1.2<D13),(C13*1.2<E13),(C13*1.2<F13),(F13*0.8>G13),(F13*0.9>H13),(C13*0.51<H13))
            if dc1 and dc2 and dc3 and dc4 and dc5 and dc6:
                dc1 = float(dc1[5])
                dc2 = float(dc2[5])
                dc3 = float(dc3[5])
                dc4 = float(dc4[5])
                dc5 = float(dc5[5])
                dc6 = float(dc6[5])
                try:
                    exec(fstring)
                except:
                    formula = False
                if formula:
                    finalList.append(row)
        screens = ScreenerData.objects.all()    
        FeaturedStocks = []       
        for companyStock in finalList:
            saveNse(companyStock)
            for screen in screens:
                if screen.symbol == companyStock[0]:
                    found = False
                    if downloadExcel('',screen.symbol):
                        found = True
                    saveStocks(companyStock,screen,found)
                    #FeaturedStocks.append(companyStock+1)
        obj = IndianStockIdeasAction.objects.get(action='Fetch Data')
        obj.status = "Success"
        obj.save()
        #redirect = '/admin/indianstockideas/indianstockideasaction/'
        #return HttpResponseRedirect(redirect)
    except Exception,e:
        print e
        obj = IndianStockIdeasAction.objects.get(action='Fetch Data')
        obj.status = "Exception: %s"%e
        obj.save()
                    
def saveNse(companyStock): 
    obj = NseData(
                symbol = companyStock[0],
                series = companyStock[1],
                open = companyStock[2],
                high = companyStock[3],
                low = companyStock[4],
                close = companyStock[5],
                last = companyStock[6],
                prevclose = companyStock[7],
                tottrdqty = companyStock[8],
                tottrdval = companyStock[9],
                timestamp = companyStock[10],
                totaltrades = companyStock[11],
                isin = companyStock[12])
    obj.save()              
                
def findCompany(company,dateData):
    for i in dateData:
        if str(i[0]).strip()== str(company).strip():
            return i
        
        
def saveStocks(companyStock,screen,flag):
    obj = FeaturedStock(
                    symbol = companyStock[0],
                    series = companyStock[1],
                    open = companyStock[2],
                    high = companyStock[3],
                    low = companyStock[4],
                    close = companyStock[5],
                    last = companyStock[6],
                    prevclose = companyStock[7],
                    tottrdqty = companyStock[8],
                    tottrdval = companyStock[9],
                    timestamp = companyStock[10],
                    totaltrades = companyStock[11],
                    isin = companyStock[12],
                    current_price = screen.current_price,
                    price_to_earning = screen.price_to_earning,
                    market_capitalization = screen.market_capitalization,
                    yoy_quarterly_profit_growth = screen.yoy_quarterly_profit_growth,
                    yoy_quarterly_sales_growth = screen.yoy_quarterly_sales_growth,
                    net_profit = screen.net_profit,
                    profit_growth_3years = screen.profit_growth_3years, 
                    profit_growth_5years = screen.profit_growth_5years,
                    sales_growth_5years = screen.sales_growth_5years,
                    sales_growth_3years = screen.sales_growth_3years,
                    ctohigh = screen.ctohigh,
                    ftw_index = screen.ftw_index,
                    cash_from_operations_last_year = screen.cash_from_operations_last_year,
                    cash_from_operations_preceding_year = screen.cash_from_operations_preceding_year,
                    recommended = flag)     
    obj.save()   
    
def getnse(screens):
    url = settings.NSE_URL
    fname = url.rsplit('/',1)[1].rsplit('.',1)[0]
    import os
    os.remove('csvfiles/'+fname)
    s=requests.get(url,stream=True)
    v = ZipFile(StringIO(s.content))
    v.extractall()
    v.extractall('csvfiles/')
    fname = url.rsplit('/',1)[1].rsplit('.',1)[0]
    commonmatches = []
    with open('csvfiles/'+fname) as f:
        for index,line in enumerate(f):
            if index == 0:
                continue
            columns = line.split(',')
            for i,screencol in enumerate(screens):
                company = screencol[0].split('/company/')[1].strip('/')
                if company.strip() == columns[0].strip():
                    commonmatches.append(columns[0:-1]+screencol[2:])
                    break

                    
	return commonmatches
	    			
def downloadExcel(url,company = 'SATIN'):
    url = "/company/"+company
    obj = ScreenerSetting.objects.filter(active=True)[0]
    session_requests = requests.session()
    result = session_requests.get(obj.login_url)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
    payload = {
        "username": obj.login_username,
        "password": obj.login_password, 
        "csrfmiddlewaretoken": authenticity_token
    }
    result = session_requests.post(obj.login_url, data = payload, headers = dict(referer = obj.login_url))
    screenerurl = obj.login_url.rsplit('/login')[0]
    apiurl = screenerurl+"/api"+url
    result = session_requests.get(apiurl, headers = dict(referer = apiurl))
    AllDict=json.loads(result.text)
    id = AllDict['warehouse_set']['id']
    downloadurl = screenerurl+"/excel/"+str(id)
    s = session_requests.get(downloadurl,stream=True)
    output = open('csvfiles/'+company+'.xls', 'wb')
    output.write(s.content)
    output.close()
    book = xlrd.open_workbook('csvfiles/'+company+'.xls')
    sheet  = book.sheet_by_name('Data Sheet')
#     headers  = sheet.row_slice(rowx=15,
#                                 start_colx=0,
#                                 end_colx=11)
    salesData  = sheet.row_slice(rowx=16,
                                start_colx=6,
                                end_colx=11)
    netProfitData  = sheet.row_slice(rowx=29,
                                start_colx=6,
                                end_colx=11)
    
    salesPreviousQuarter = sheet.cell(41,6).value
    salesCurrentQuarter = sheet.cell(41,10).value
    netProfitPreviousQuarter = sheet.cell(48,6).value
    netProfitCurrentQuarter = sheet.cell(48,10).value
    
    sales = [i.value for i in salesData]
    netProfit = [i.value for i in netProfitData]
    dataQuery = obj.datasheet_query
    try:
        exec(dataQuery)
    except:
        featured = False
    return featured
   
   
def getscreener():
    obj = ScreenerSetting.objects.filter(active=True)[0]
    session_requests = requests.session()
    result = session_requests.get(obj.login_url)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
    payload = {
	    "username": obj.login_username,
	    "password": obj.login_password, 
	    "csrfmiddlewaretoken": authenticity_token
	}
    result = session_requests.post(obj.login_url, data = payload, headers = dict(referer = obj.login_url))
    result = session_requests.get(obj.api_url+obj.query, headers = dict(referer = obj.api_url+obj.query))
    AllDict=json.loads(result.text)
    resultList = AllDict['page']['results']
    url = obj.api_url+obj.query
    count = int(AllDict['page']['total'])+1
    for i in range(2,count):
        newurl = url+"&page="+str(i)
        endData = session_requests.get(newurl, headers = dict(referer = newurl))
        outDict=json.loads(endData.text)
        inner = outDict['page']['results']
        resultList = resultList+inner
    return resultList