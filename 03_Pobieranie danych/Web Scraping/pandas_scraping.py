
import pandas as pd
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

link_1 = "https://www.gddkia.gov.pl/pl/2783/zamowienia-publiczne-rozstrzygniete,oddzial-1"
link_2 =  "https://tge.pl/energia-elektryczna-rdn?dateShow=15-04-2020&dateAction=prev"
link_3 = "https://www.gddkia.gov.pl/ajax/zamowieniePubliczneSzczegoly.php?id=26488&lang=pl"
pd.read_html(link_3, encoding="utf8")[0]

main_url = "https://www.gddkia.gov.pl"
# df = pd.read_html(link_2)[0]
response = requests.get(link_1)
soup = BeautifulSoup(response.text, "html.parser")
table_1 = soup.findAll('table')[0]

all_link = table_1.findAll('a')

all_link[0]

pd.read_html(main_url + all_link[0]['href'], encoding='utf8')[0]

response_project = requests.get(main_url + all_link[0]['href'])

soup_project = BeautifulSoup(response_project.text, "html.parser")
# pliki do pobrania
for link_ in soup_project.findAll('a'):
    try:
        title = link_['title']

    except:
        title = ""
    if title == "Pobierz plik: Ogloszenie-o-zamowieniu.pdf":
        print(main_url + link_['href'])
        urllib.request.urlretrieve(main_url + link_['href'], 'download_1.pdf')

print('done')