import re
import time
import urllib3
import requests
from bs4 import BeautifulSoup as bss

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.108 Safari/537.36'}

url = "https://auto.ru/cars/audi/a8/2305474/all/?sort=fresh_relevance_1-desc&output_type=list&page=1"
page = requests.get(url, headers=headers)
soup = bss(page.content, 'html.parser')
http = urllib3.PoolManager()
response = http.request('GET', url)
s_link = bss(response.data)
for link in s_link.findAll('a', aattrs={'href': re.compile("^http://")}):
    print(link.get('href'))
#for links in soup.find_all("div", {"class": "ListingCarsPagination-module__container"}):
#    print(links)

#for each_div in soup.find_all("div", {"class": "ListingItemPrice-module__content"}):
#    print(each_div)
