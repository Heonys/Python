import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

sp = BeautifulSoup(res.text, "lxml")
webtoon = sp.find_all('a', attrs={'class':'title'})

for index in webtoon:
    print(index.get_text())