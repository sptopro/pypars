import time

import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.108 Safari/537.36'}

url = 'https://auto.ru/cars/audi/a8/2305474/all/?sort=fresh_relevance_1-desc&output_type=list&page=1'
page = requests.get(url, headers=headers)
soup = bs(page.content, 'html.parser')
url_1 = soup.findAll('a', {'class': 'page-link', 'rel': 'next'})
print(url_1)

#for each_div in soup.findAll("div", {"class": "ListingItemPrice-module__content"}):
#    print(each_div)
