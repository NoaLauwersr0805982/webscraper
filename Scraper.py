import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time as t
import redis as redis


def RedisCatcher(elemlist1):
    scraper_df = pd.DataFrame(elemlist1, columns=['Hash', 'Time', 'Bitcoin', 'US Dollar'])

    red = redis.Redis(host='redis',port=6379, db=0)

    red.set('scraperdf', scraper_df.to_json())
    


def ElementsCatcher(Elements):

    elemlist1 = []

    for Element in Elements:

        Hash = Element.find('a')

        elemlist2 = []
        elemlist2.append(Hash.text)

        TiBitDollar = Element.find_all('span')
        
        nottext = ('Hash', 'Time', 'Amount (BTC)', 'Amount (USD)')

        for data in TiBitDollar:
            if (data.text not in nottext):
                elemlist2.append(data.text)

        elemlist2[3] = elemlist2[3].replace(',', '')
        elemlist2[3] = elemlist2[3].replace('$', '')
        elemlist2[3] = float(elemlist2[3])

        elemlist1.append(elemlist2)

        RedisCatcher(elemlist1)

    print(elemlist1)


def MainScraper():
    url = 'https://www.blockchain.com/btc/unconfirmed-transactions'

    request = requests.get(url)

    soup = BeautifulSoup(request.text, 'html.parser')

    Elements = soup.find_all('div', class_='hXyplo')
    ElementsCatcher(Elements)

MainScraper()

while True:

    MainScraper()
    t.sleep(60)
