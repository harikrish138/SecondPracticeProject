from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
driver.maximize_window()
driver.find_element(By.ID, "btn1").click()
wait=WebDriverWait(driver,20,4)
wait.until(expected_conditions.visibility_of_element_located((By.ID, "txt1"))).send_keys("hari")
driver.find_element(By.ID, "btn2").click()
wait.until(expected_conditions.visibility_of_element_located((By.ID, "txt2"))).send_keys("krishna")
sleep(3)
driver.close()
# "//div[@id='content-wrapper']/div/div/div[2]/div/div/div/div/article/div/h3/input[1]"





