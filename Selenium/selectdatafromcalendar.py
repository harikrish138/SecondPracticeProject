from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
month="//*[@class='ui-datepicker-title']/span[1]"
year="//*[@class='ui-datepicker-title']/span[2]"
days="//*[@class='ui-datepicker-calendar']/tbody/tr/td"
left_arrow="//*[@class='ui-datepicker-prev ui-corner-all']/span"
right_arrow="//*[@class='ui-datepicker-next ui-corner-all']/span"
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
ops.add_argument("--disable-ads")
driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(10)

driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")

def select_date(DAY,MONTH,YEAR):
    wait = WebDriverWait(driver, 15)
    year1=driver.find_element(By.XPATH,year).text
    month1=driver.find_element(By.XPATH,month).text
    act=ActionChains(driver)
    MonthsList=['january','february','march','april','may','june','july','august','september','october','november','december']
    if year1>=YEAR :
        while True:
            if year1 == YEAR:
                break
            wait.until(EC.presence_of_element_located((By.XPATH,left_arrow)))
            driver.find_element(By.XPATH,left_arrow).click()
            year1 = driver.find_element(By.XPATH, year).text

        if month1.lower() in MonthsList:
            while True:
                if month1.lower() == MONTH.lower():
                    break
                sleep(10)
                wait.until(EC.presence_of_element_located((By.XPATH,left_arrow)))
                prev_btn = wait.until(EC.element_to_be_clickable((By.XPATH, left_arrow)))
                driver.execute_script("arguments[0].scrollIntoView(true);", prev_btn)
                prev_btn.click()
                # month_element=driver.find_element(By.XPATH,left_arrow)
                # act.move_to_element(month_element).click().perform()
                wait.until(EC.presence_of_element_located((By.XPATH, month)))
                month1 = driver.find_element(By.XPATH, month).text

        else:
            print('month not found')
        if DAY < '31':
            wait.until(EC.presence_of_all_elements_located((By.XPATH, days)))
            dates = driver.find_elements(By.XPATH, days)
            for i in dates:
                day=i.text
                if DAY == day:
                    wait.until(EC.element_to_be_clickable((By.XPATH, days)))
                    i.click()
                    print(day,month1,year1)
        else:
            print('please give valid day')

    if year1<YEAR:
        while True:
            if year1 == YEAR:
                break
            wait.until(EC.element_to_be_clickable((By.XPATH, left_arrow)))
            driver.find_element(By.XPATH,right_arrow).click()
            year1 = driver.find_element(By.XPATH, year).text

        if month1.lower() in MonthsList:
            while True:
                if month1.lower() == MONTH.lower():
                    break
                prev_btn = wait.until(EC.element_to_be_clickable((By.XPATH, left_arrow)))
                driver.execute_script("arguments[0].scrollIntoView(true);", prev_btn)
                prev_btn.click()
                month1 = driver.find_element(By.XPATH, month).text

        else:
            print('month not found')
        if DAY < '31':
            wait.until(EC.presence_of_all_elements_located((By.XPATH, days)))
            dates = driver.find_elements(By.XPATH, days)
            for i in dates:
                day=i.text
                if DAY == day:
                    wait.until(EC.element_to_be_clickable((By.XPATH, days)))
                    i.click()
                    print(day,month1,year1)

        else:
            print('please give valid day')

driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"Selenium Practice").click()
# driver.find_element(By.LINK_TEXT,"Calendars Practice").click()
# driver.find_element(By.ID,"first_date_picker").click()
# select_date('23','march','2025')
driver.find_element(By.ID,"third_date_picker").click()
select_date('23','march','2025')
driver.quit()


