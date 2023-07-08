from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup as Soup 
driver = webdriver.Chrome("./flasktest/chromedriver.exe")
driver.get('https://www.instagram.com/')
time.sleep(2)
email=driver.find_element(By.NAME, "username")
password=driver.find_element(By.NAME, "password")
email.send_keys('testing_ac_c')
password.send_keys('testingacc')
button=driver.find_element(By.CLASS_NAME,"_acan._acap._acas._aj1-")
button.click()
time.sleep(2)
search_name=input("account:")
driver.get("https://www.instagram.com/"+search_name)
post_url = []
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
    time.sleep(2) # 等待網頁加載
check=0
summ=0
for url in post_url :
    check=0
    find=False
    while not find:
        try:
            post_elem = driver.find_element(By.XPATH, '//a[@href="'+str(url)+'"]')
            action = ActionChains(driver)
            action.move_to_element(post_elem).perform()
            driver.find_elements(By.CLASS_NAME,'_ac2d')
            try:
                n_like_elem =driver.find_elements(By.CLASS_NAME,'_abpm')
                n_like = n_like_elem[0].text
                n_comment = n_like_elem[1].text
                find=True
                print(n_like)
            except:
                print("error")
                break
            
        except:
            scroll = 'window.scrollBy(0,-250)'
            driver.execute_script(scroll)
            continue    