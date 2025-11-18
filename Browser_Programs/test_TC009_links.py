from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.hyrtutorials.com/")
wait = WebDriverWait(driver,20,2)
driver.refresh()
all_links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'a')))
# all_links = driver.find_elements(By.TAG_NAME,'a')
brkn_count=0
un_brkn_count=0
# if len( all_links)>1:
#     for i in all_links:
#         url = i.get_attribute("href")
#         print(url)
#         brkn_count+=1
# else:
#     print("no links found")

for link in all_links:
    try:
        wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
        url = link.get_attribute("href")
        if url is None =="":
            continue
        res = requests.head(url,timeout=5)
        if res.status_code >= 400:
            print(url,"It is broken link")
            brkn_count +=1
        else:
            # print(url,"It is not a broken link")
            un_brkn_count +=1
    except Exception as e:
        print("Error processing link",e)
        continue
print(brkn_count)
print(un_brkn_count)
sleep(3)
driver.close()
