import requests
import re

from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

res = requests.get(url, headers=headers)
res.raise_for_status()

sp = BeautifulSoup(res.text,'lxml')



items = sp.find_all('li',attrs={'class':re.compile('^search-product')})
print(items[0].find('div', attrs={'class':'name'}).get_text())
