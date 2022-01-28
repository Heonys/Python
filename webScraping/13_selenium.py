from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome() 
browser.get('https://www.naver.com/')

# 로그인 창 
# elem = browser.find_element_by
# elem.click()

elem = browser.find_element_by_id('query')
elem.send_keys("롤챔스")
elem.send_keys(Keys.ENTER)