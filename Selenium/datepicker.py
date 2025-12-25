from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
ops.add_argument("--disable-ads")
driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(10)

driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")
driver.maximize_window()

driver.find_element(By.ID,"third_date_picker").click()

def select_date(month,day,year):
    driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']").click()
    select=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
    select.select_by_visible_text(month)
    driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']").click()
    select=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
    select.select_by_value(year)
    dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td")
    days="//table[@class='ui-datepicker-calendar']/tbody/tr/td"
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, days)))
    dates = driver.find_elements(By.XPATH, days)
    for i in dates:
        if day == i.text:
            wait.until(EC.element_to_be_clickable((By.XPATH, days)))
            i.click()
            print(day,month,year)
select_date('Oct','13','2026')
sleep(2)
driver.quit()