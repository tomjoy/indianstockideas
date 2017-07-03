from lxml import etree
import urllib

# web = urllib.urlopen("http://www.moneycontrol.com/bse/shareholding/institutional_holding.php?type=1&pno=1")
# s = web.read()
# 
# html = etree.HTML(s)
# 
# ## Get all 'tr'
# tr_nodes = html.xpath('//table[@class="b_12 dvdtbl"]/tr')
# 
# ## 'th' is inside first 'tr'
# header = [i[0].text for i in tr_nodes[0].xpath("th")]
# 
# ## Get text from rest all 'tr'
# td_content = [[[td.xpath('a')[0].xpath('strong')[0].text,td.xpath('a')[0].get('href')] if td.xpath('a') else td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]
# print td_content
# for i in range(1,10):
#     MONEYCONTROL_URL = 'http://www.moneycontrol.com/stocks/marketstats/hidivyields.php?optex=NSE&indcode='+str(i)+'&group=All'
#     web = urllib.urlopen(MONEYCONTROL_URL)
#     s = web.read()
#      
#     html = etree.HTML(s)
#      
#     ## Get all 'tr'
#     span_nodes = html.xpath('//span[@class="gld13 disin"]')
#      
#     ## 'th' is inside first 'tr'
#     #header = [i[0].text for i in tr_nodes[0].xpath("th")]
#      
#     ## Get text from rest all 'tr'
#     stock_urls = [span.xpath('a')[0].get('href') for span in span_nodes]
#     for url in stock_urls:
#         web = urllib.urlopen(url)
#         s = web.read()
#      
#         html = etree.HTML(s)
# 
#         div_nodes = html.xpath('//div[@class="FL gry10"]//text()')
#         print div_nodes[7],div_nodes[2].split(': ')[1],url,url.split('/')[5],url.split('/')[6],url.split('/')[7]
#     

def moneycontrolfunding():
    featured = FeaturedStock.objects.filter(recommended = True)
    for obj in featured:
        symbol = obj.symbol
        obj = MoneyControlMapping.objects.get(stockname=symbol)
        mutualfundcode = obj.urlsplit3
        url = settings.MONEYCONTROL_FUNDS
        web = urllib.urlopen(MONEYCONTROL_URL)
        s = web.read()
         
        html = etree.HTML(s)
        
        span_nodes = html.xpath('//div[@id="div_0"]/div/table[@class="tblfund2"]/tbody/tr[last()]')
        stock_urls = [span.xpath('td')[0].text  for span in span_nodes if span.xpath('td')[0].text]
        
moneycontrolfunding()