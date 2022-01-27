import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=557672&no=385&weekday="
res = requests.get(url)
res.raise_for_status()

sp = BeautifulSoup(res.text, "lxml")

td = sp.find_all('td',attrs={'class':'title'})

for index in td:
    print(index.a.get_text())