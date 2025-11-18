from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[.='Click for JS Alert']").click()
alert=driver.switch_to.alert
print(f"First alert {alert}")

alert.accept()
sleep(3)

driver.find_element(By.XPATH,"//button[.='Click for JS Confirm']").click()
alert=driver.switch_to.alert
print(f"Second alert {alert}")
sleep(3)
alert.dismiss()

driver.find_element(By.XPATH,"//button[.='Click for JS Prompt']").click()
alert=driver.switch_to.alert
alert.send_keys("welcome to alerts")
print(f"Third alert {alert}")
sleep(3)
alert.accept()
sleep(3)
driver.close()