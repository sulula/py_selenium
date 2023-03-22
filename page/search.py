import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Search:
    def __init__(self, driver):
        self.driver = driver

    def search_str(self):
        e = self.driver.find_element(By.XPATH, "(//div['id=content_left']/div/h3/a)[0]")
        # e = self.driver.find_element(By.XPATH, "//tr/td/span['class=op_dict3_font24 op_dict3_marginRight c-gap-right']")
        return e

    def search_number(self):
        e = self.driver.find_element(By.XPATH, "//h3['class=.c-title']/a")

        print(e)
        return e
