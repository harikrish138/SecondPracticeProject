
from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser', action='store',default='chrome',help='chrome, firefox and edge')
@pytest.fixture(scope='function')
def browser(request):
    browser_name=request.config.getoption('--browser')
    if browser_name.lower() == 'chrome':
        driver=webdriver.Chrome()
    elif browser_name.lower() == 'firefox':
        driver=webdriver.Firefox()
    elif browser_name.lower()=='edge':
        driver= webdriver.Edge()
    else:
        raise Exception(f'browser is {browser_name} not available')
    driver.maximize_window()
    yield driver
    driver.quit()

def test_openBrowser(browser):
    browser.get('https://google.com')