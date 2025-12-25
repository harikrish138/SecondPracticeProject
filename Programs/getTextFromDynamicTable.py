from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
browser_name='Chrome'
elements=driver.find_elements(By.XPATH,"//*[@id='rows']/tr")
for j in elements:
    actual_name = j.find_element(By.XPATH,"./td[1]").text
    if actual_name == browser_name:
        print(j.find_element(By.XPATH,"./td[5]").text)
