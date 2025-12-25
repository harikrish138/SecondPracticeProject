from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.ilovepdf.com/word_to_pdf')
driver.maximize_window()
file_input=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@type='file']")))
file_input.send_keys(r"C:\\Users\\sandr\\Desktop\\Harikrishna's Job details\\Harikrishna_5_1_Years_ExP.docx")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "processTask"))).click()
sleep(15)
driver.quit()




