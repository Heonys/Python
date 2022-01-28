from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome() 
browser.maximize_window() #창 최대화
browser.get('https://www.naver.com/')



elem = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH, "")))


