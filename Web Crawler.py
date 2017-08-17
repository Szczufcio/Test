import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = "http://allegro.pl/muzyka?p=" + str(page)
        source_code = request.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll("a", {'class' : "offer-title"}):
            href = link.get('href')
            print(href)

trade_spider(1)