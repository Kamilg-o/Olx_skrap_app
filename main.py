from bs4 import BeautifulSoup
from requests import get


url='https://www.olx.pl/oferty/q-samochody-osobowe/'

page= get(url)
bs = BeautifulSoup(page.content)