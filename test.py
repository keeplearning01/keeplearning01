from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup 
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(2)
email=driver.find_element(By.NAME, "username")
password=driver.find_element(By.NAME, "password")
email.send_keys('chang_bo_guan')
password.send_keys('?8572478')
button=driver.find_element(By.CLASS_NAME,"_acan._acap._acas._aj1-")
button.click()
time.sleep(2)
driver.get("https://www.instagram.com/raylee_0510")
time.sleep(2)
html = driver.page_source
soup = Soup(html, 'lxml')
title=soup.select('span._ac2a _ac2b')
x=0
for i in title:
     if(x==1):
          print(i['title'])
     print(i.span.text)
     x+=1