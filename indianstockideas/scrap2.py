from StringIO import StringIO
from zipfile import ZipFile
import requests
s=requests.get('https://www.nseindia.com/content/historical/EQUITIES/2016/NOV/cm08NOV2016bhav.csv.zip',stream=True)
v = zipfile.ZipFile(StringIO.StringIO(s.content))
v.extractall()
v.extractall('/home/tom/Music/geoip/')

