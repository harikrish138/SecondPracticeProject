from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.maximize_window()
driver.switch_to.frame("frm1")
dropdown=driver.find_element(By.ID,"selectnav1")
selct=Select(dropdown)
selct.select_by_visible_text("- Java")
driver.switch_to.parent_frame()
driver.switch_to.frame('frm2')
driver.find_element(By.XPATH,"//*[@id='firstName']").send_keys('krishna')
driver.find_element(By.XPATH,"//*[@id='lastName']").send_keys('hari')
sleep(3)
driver.close()

