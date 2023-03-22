from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from conftest import driver
from page.search import Search


class Home:

    # def __init__(self):
    # self.driver = webdriver.Chrome()
    # self.driver.implicitly_wait(5)\=
    # self.wait = WebDriverWait(self.driver, 30)
    # # 1 | open | / |  |
    # self.driver.get("https://www.baidu.com/")
    # # 2 | setWindowSize | 1332x746 |  |
    # self.driver.set_window_size(1332, 746)

    def search(self, keyword=None):
        input_ele = driver.find_element(By.ID, "kw")
        input_ele.click()
        input_ele.clear()
        input_ele.send_keys(keyword)
        input_ele.send_keys(Keys.ENTER)
        return Search(driver)
