import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
res = requests.get(url, headers=headers)
res.raise_for_status()

#class="weather_graphic"
#temperature_text
soup = BeautifulSoup(res.text, 'lxml')
print("서울의 현재온도 ",soup.find('div',attrs={'class':'weather_graphic'}).find('div',attrs={'class':'temperature_text'}).get_text())

