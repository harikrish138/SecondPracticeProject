
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ops= Options()
ops.add_argument("--headless")
driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(6)
driver.get("https://www.amazon.com")
element=driver.find_element(By.CSS_SELECTOR,"img[alt='Deals in Computers']")
driver.execute_script("arguments[0].scrollIntoView(true);",element)
driver.quit()

