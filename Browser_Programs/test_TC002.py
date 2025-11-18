from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
ops= webdriver.ChromeOptions() 
ops.add_argument("--disable-ads")
driver = webdriver.Chrome(options = ops)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@placeholder='Username']").clear()
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys('Admin')
driver.find_element(By.XPATH,"//input[@placeholder='Password']").clear()
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('admin123')
driver.find_element(By.XPATH,"//*[.=' Login ']").click()
sleep(3)
driver.close()



