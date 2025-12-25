from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
driver.maximize_window()
mainwindow=driver.current_window_handle
driver.set_window_size(1080,720)

driver.switch_to.new_window('tab')
driver.get("https://www.flipkart.com")

driver.switch_to.new_window('tab')
driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to.new_window('tab')
driver.get("https://www.flipkart.com")

driver.switch_to.new_window('tab')
driver.get("https://www.facebook.com")
driver.switch_to.window(mainwindow)
windows=driver.window_handles
for i in windows:
    if i != mainwindow:
        driver.switch_to.window(i)
        print(driver.title)
sleep(3)
# driver.switch_to.window(mainwindow)
# sleep(3)
# print(driver.title)
#
# windows=driver.window_handles
# for i in windows:
#     driver.switch_to.window(windows[-1])
# print(driver.title)
driver.quit()