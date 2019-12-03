import json

import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.108 Safari/537.36'}

url = "https://auto.ru/cars/audi/a8/2305474/all/?sort=fresh_relevance_1-desc&output_type=list&0"


#page = requests.get(url, headers=headers)
def getLinks(url):
    global links
    links = []
    page = requests.get(url)
    data = page.text
    soup = bs(data)
    for link in soup.find_all('a', {"class": "Button Button_color_whiteHoverBlue Button_size_s Button_type_link Button_"
                                             "width_default ListingPagination-module__page"}):
        links.append(link.get('href'))
    return links


print(getLinks(url))

page = requests.get(url, headers=headers)
soup = bs(page.content, 'html.parser')

for i in getLinks(url):
    result = [soup.find_all("div", {"class": "ListingItemPrice-module__content"})]
    print(result)
