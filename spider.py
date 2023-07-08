from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup as Soup 

BROWSER = None

def startBrowser():
    global BROWSER

    if BROWSER != None:
        return
    else:
        BROWSER = webdriver.Chrome()
        time.sleep(2)


    # if os.path.exists(os.getcwd() + '/cookie'):
    #     with open(os.getcwd() + "/cookie") as file:
    #         data = file.read()

    #     BROWSER.add_cookie(json.loads(data))

    # BROWSER.get('https://www.instagram.com/')

    # if not os.path.exists(os.getcwd() + '/cookie'):
        # time.sleep(2)
    # email=BROWSER.find_element(By.NAME, "username")
    # password=BROWSER.find_element(By.NAME, "password")
    # email.send_keys('testing_ac_c')
    # password.send_keys('testingacc')
    # button=BROWSER.find_element(By.CLASS_NAME,"_acan._acap._acas._aj1-")
    # button.click()
    # time.sleep(2)

    # cookies = json.dumps(BROWSER.get_cookies())
    # with open(os.getcwd() + "/cookie", "w") as file:
    #     file.write(cookies)

def get_like_post(search_name):
    BROWSER = webdriver.Chrome()
    BROWSER.get("https://www.instagram.com/"+search_name)
    post_url = []
    time.sleep(1)
    html = BROWSER.page_source
    soup = Soup(html, 'lxml')
    title=soup.select('span._ac2a')
    x=0
    follower=None
    for i in title:
        if(x==1):
            follower=i['title']
        x+=1
    for i in range(5):
        BROWSER.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)
        html = BROWSER.page_source
        soup = Soup(html, 'lxml')
            # 尋找所有的貼文連結
        for elem in soup.select('article div div div div a'):
                # 如果新獲得的貼文連結不在列表裡，則加入
            if elem['href'] not in post_url:
                post_url.append(elem['href'])
        time.sleep(3) 
    summ=0
    sumc=0
    not_post=0
    post_num=len(post_url)
    for url in post_url :
        find=False
        while not find:
            try:
                post_elem = BROWSER.find_element(By.XPATH, '//a[@href="'+str(url)+'"]')
                action = ActionChains(BROWSER)
                action.move_to_element(post_elem).perform()
                BROWSER.find_elements(By.CLASS_NAME,'_ac2d')
                try:
                    n_like_elem =BROWSER.find_elements(By.CLASS_NAME,'_abpm')
                    n_like = n_like_elem[0].text
                    n_c=n_like_elem[1].text
                    summ+=int(n_like)
                    sumc+=int(n_c)
                    find=True
                except:
                    not_post+=1
                    break
                
            except:
                scroll = 'window.scrollBy(0,-250)'
                BROWSER.execute_script(scroll)
                continue 
    
    result={"like":summ,"n_c":sumc,"followers":follower,"post_num":post_num,"not_post":not_post}  
    return result

# if __name__ == "__main__":
#     startBrowser()
#     print(get_like('ye06_15'))
#     while True:
#         time.sleep(1)

