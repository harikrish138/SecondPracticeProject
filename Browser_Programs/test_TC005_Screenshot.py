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
driver.find_element(By.XPATH,"//form[@class='oxd-form']/div[1]/div/div[2]/input").clear()
driver.find_element(By.XPATH,"//form[@class='oxd-form']/div[1]/div/div[2]/input").send_keys('Admin')
driver.find_element(By.XPATH,"//form[@class='oxd-form']/div[2]/div/div[2]/input").clear()
driver.find_element(By.XPATH,"//form[@class='oxd-form']/div[2]/div/div[2]/input").send_keys('admin')
driver.find_element(By.XPATH,"//form[@class='oxd-form']/div[3]/button").click()
try:
    dashboard_web_element = driver.find_element(By.XPATH,
                                                "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    if dashboard_web_element.is_displayed():
        print('login successful')
        driver.close()
    else:
        driver.save_screenshot("C:/Users/91738/PycharmProjects/DemoProject/SecondPracticeProject/Screenshot/photo1.png")
        driver.quit()
except Exception:
    print(Exception)
    driver.save_screenshot("C:/Users/91738/PycharmProjects/DemoProject/SecondPracticeProject/Screenshot/photo1.png")
    driver.quit()
    sleep(3)




