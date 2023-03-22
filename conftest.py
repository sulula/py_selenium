import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


# fixture级别之session
@pytest.fixture(scope='module', autouse=True)
def driver():
    return webdriver.Chrome()


@pytest.fixture(scope='module', autouse=True)
def init(driver):
    driver.maximize_window()
    driver.get('http://www.baidu.com/')
    # 隐性等待
    driver.implicitly_wait(20)
    yield
    driver.quit()
