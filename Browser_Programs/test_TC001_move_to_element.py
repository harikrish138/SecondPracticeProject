
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
ops=webdriver.ChromeOptions()

ops.add_argument("--disable-ads")
driver = webdriver.Chrome(options=ops)
driver.get("https://www.hyrtutorials.com/")

driver.implicitly_wait(10)
driver.maximize_window()
chain=ActionChains(driver)
selenium_link_element=driver.find_element(By.XPATH,"//ul[@id='nav1']/li[4]/a")
chain.move_to_element(selenium_link_element).perform()
# links=driver.find_elements(By.XPATH,"//div[@id='LinkList210']/ul/li[4]/ul/li/a")
dropdown=driver.find_element(By.XPATH,"//*[@id='LinkList210']/ul/li[4]/ul/li[3]/a")
dropdown.click()
# for i in links:
#     if i.text == 'XPath Practice':
#         i.click()
#         break
#     else:
#         print('link not found')
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div/input[1]").clear()
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div/input[1]").send_keys("hari")
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div/input[2]").send_keys("sowmyanadh")
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div/input[3]").send_keys("sowmyanadh123@gmai.com")
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div/div[2]/input").send_keys("Hari123@")
driver.find_element(By.XPATH,"//*[@id='post-body-299858861183690484']/div/form/div/input[4]").send_keys("Hari123@")
driver.find_element(By.XPATH,"//*[.='Register' and @class='btn']").click()

driver.close()

