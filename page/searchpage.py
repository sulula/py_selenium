import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Search:
    # @pytest.mark.usefixtures
    def search_by(self, driver, keyword=None):
        input_ele = driver.find_element(By.ID, "kw")
        input_ele.click()
        input_ele.clear()
        input_ele.send_keys(keyword)
        input_ele.send_keys(Keys.ENTER)
        return self

    # @pytest.mark.usefixtures
    def search_str(self, driver, keyword):
        self.search_by(driver, keyword)
        e = driver.find_element(By.XPATH, "//h3/a")
        # e = driver.find_element(By.XPATH, "//tr/td/span['class=op_dict3_font24 op_dict3_marginRight c-gap-right']")
        print(e)
        return e

    # @pytest.mark.usefixtures
    def search_number(self, driver, keyword):
        self.search_by(driver, keyword)
        time.sleep(20)
        e = driver.find_element(By.XPATH, "//h3/a")
        print(e)
        return e
