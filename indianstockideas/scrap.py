
import requests
from lxml import html

USERNAME = "gittopaul2@gmail.com"
PASSWORD = "a12345"

LOGIN_URL = "https://www.screener.in/login/"
URL = "https://www.screener.in/api/screens/query/?query=Current+ratio+%3E+1.2+AND%0D%0AEPS+%3E+EPS+last+year+AND%0D%0ASales+last+year+%3E+Sales+preceding+year+AND%0D%0ANet+Profit+last+year+%3E+Net+Profit+preceding+year+AND%0D%0AMarket+Capitalization+%3E+5+AND%0D%0ANet+Profit++%3E+10+AND%0D%0ANet+Profit+last+year+%3E+5+AND%0D%0Acurrenttohigh+%3C+81"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    #tree = html.fromstring(result.content)
    #bucket_names = tree.xpath("//body/text()")
    import json
    j=json.loads(result.text)
    print type(j),j

if __name__ == '__main__':
    main()
    
    
#         for index,line in enumerate(f):
#             if index == 0:
#                 continue
#             columns = line.split(',')
#             
#             for screencol in screens['page'].get('results',[]):
#                 company = screencol[0].split('/company/')[1].strip('/')
#                 if company == columns[0]:
#                     commonmatches.append([columns[0]]+screencol[1:]+columns[1:])
