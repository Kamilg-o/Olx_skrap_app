from bs4 import BeautifulSoup
from requests import get


url='https://www.olx.pl/motoryzacja/samochody/bmw/q-samochody-osobowe/'

page= get(url)
bs = BeautifulSoup(page.content)

for offer in bs.find_all(class_="offer-wrapper"):
    name = offer.find_all("strong")
    location = offer.find_all("small",class_="breadcrumb")[1]
    city = location.find("span").get_text()
    print(name[0].get_text())
    print(name[1].get_text(),city)
    print("")
