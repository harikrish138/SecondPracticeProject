# from gettext import textdomain
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_attribute

driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

a = driver.find_element(By.XPATH, "//div[@id='content']/div/p")
sleep(2)
print(a.text)
driver.close()