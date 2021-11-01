from bs4 import BeautifulSoup
from requests import get


url='https://www.olx.pl/motoryzacja/samochody/bmw/q-samochody-osobowe/'

page= get(url)
bs = BeautifulSoup(page.content,"html.parser")

for offer in bs.find_all(class_="offer-wrapper"):
    name = offer.find_all("strong")
    location = offer.find_all("small",class_="breadcrumb")[1]
    city = location.find("span").get_text()
    url_offer = offer.find("a")
    offer_page=get(url_offer["href"])
    bs1=BeautifulSoup(offer_page.content,"html.parser")
    print(name[0].get_text())
    print(name[1].get_text(), city)
    for offer_in_page in bs1.find_all("p",class_="css-xl6fe0-Text eu5v0x0"):
        print(offer_in_page.get_text())
    print("")


