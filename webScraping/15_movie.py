import requests
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
url = "https://play.google.com/store/movies"
req = requests.get(url, headers=headers)
req.raise_for_status() 
soup = BeautifulSoup(req.text, 'lxml')

print(soup.text)



