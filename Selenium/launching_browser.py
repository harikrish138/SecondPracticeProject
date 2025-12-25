from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome()
# driver.get('https://www.facebook.com')
# sleep(3)
# driver.quit()
#
service=Service("C:/Users/sandr/OneDrive/Desktop/StoreRoom/drivers/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get('https://www.facebook.com')
# sleep(3)
driver.quit()

