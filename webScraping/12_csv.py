import csv
import requests
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = '시가총액.csv'
f= open(filename, 'w', encoding='utf-8-sig', newline="")
writer = csv.writer(f)

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
writer.writerow(title)


for page in range(1,6):
    res = requests.get(url+str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    rows = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')
    

    for row in rows:
        cols = row.find_all('td')
        if len(cols) <=1:
            continue

        data = [col.get_text().strip() for col in cols]
        writer.writerow(data)








