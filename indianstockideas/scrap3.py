from lxml import etree
import urllib

web = urllib.urlopen("http://www.moneycontrol.com/bse/shareholding/institutional_holding.php?type=1&pno=1")
s = web.read()

html = etree.HTML(s)

## Get all 'tr'
tr_nodes = html.xpath('//table[@class="b_12 dvdtbl"]/tr')

## 'th' is inside first 'tr'
header = [i[0].text for i in tr_nodes[0].xpath("th")]

## Get text from rest all 'tr'
td_content = [[[td.xpath('a')[0].xpath('strong')[0].text,td.xpath('a')[0].get('href')] if td.xpath('a') else td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]
print td_content
