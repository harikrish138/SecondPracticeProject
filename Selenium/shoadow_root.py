from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.google.com')
element=driver.find_element(By.XPATH , "//*[@name='q']")
element.send_keys('hello')
driver.close()





#  //span[text()='iPhone 15 (128 GB) - Blue']/ancestor::div[@data-component-type='s-search-result']//span[@class='a-price-whole']
