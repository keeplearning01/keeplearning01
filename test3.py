
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/raylee_0510")
post_url = []
time.sleep(1)
html = driver.page_source
soup = Soup(html, 'lxml')
title=soup.select('span._ac2a')
for i in range(5):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    html = driver.page_source
    soup = Soup(html, 'lxml')
            # 尋找所有的貼文連結
    for elem in soup.select('article div div div div a'):
            # 如果新獲得的貼文連結不在列表裡，則加入
        if elem['href'] not in post_url:
            post_url.append(elem['href'])
    time.sleep(3)
summ=0
for url in post_url :
    find=False
    while not find:
        try:
            post_elem = driver.find_element(By.XPATH, '//a[@href="'+str(url)+'"]')
            action = ActionChains(driver)
            action.move_to_element(post_elem).perform()
            driver.find_elements(By.CLASS_NAME,'_ac2d')
            try:
                n_like_elem = driver.find_elements(By.CLASS_NAME,'_abpm')
                n_like = n_like_elem[0].text
                summ+=int(n_like)
                n_c=n_like_elem[1].text
                find=True
            except:
                break      
        except:
            scroll = 'window.scrollBy(0,-250)'
            driver.execute_script(scroll)
            continue 
print(summ)