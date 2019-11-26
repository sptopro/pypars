import requests
from bs4 import BeautifulSoup

def drug_data():
    url = 'https://auto.ru/cars/audi/a8/2305474/all/?sort=fresh_relevance_1-desc&output_type=list&'

    while url:
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text ,"lxml")

        #data = soup.select('name-head a')
        #for link in data:
        #    href = 'https://www.drugbank.ca/drugs/' + link.get('href')
        #    pages_data(href)

        # next page url
        url = soup.findAll('a', {'class': 'page-link', 'rel': 'next'})
        print(url)
        if url:
            url = 'https://www.drugbank.cahttps://auto.ru/cars/audi/a8/2305474/all/?sort=fresh_relevance_1-desc&output_type=list&' + url[0].get('href')
        else:
            break

drug_data()