from bs4 import BeautifulSoup
from requests import get


url='https://www.olx.pl/motoryzacja/samochody/bmw/q-samochody-osobowe/'

page= get(url)
bs = BeautifulSoup(page.content)

for offer in bs.find_all("strong"):
    print(offer.text)