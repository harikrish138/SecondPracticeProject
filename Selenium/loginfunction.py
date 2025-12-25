from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ops=Options()
ops.add_argument('--headless')  # Headless mode
driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//*[.='Login']").click()

driver.quit()


