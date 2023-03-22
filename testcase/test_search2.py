import os
import pytest
from selenium import webdriver
from allure_pytest import plugin as allure_plugin

from page.home import Home


class TestCase:

    def setup(self):
        # global home
        self.home = Home()

    def test_string(self):
        module = self.home.search("test")
        ele = module.search_str()
        print('test_string', ele.text)
        assert ele.text == "test"

    # def test_number(self):
    #     module = self.home.search(1)
    #     ele = module.search_number()
    #     print('test_number')
    #     assert ele.get_attribute('aria-label').find("1") >= 0
    #
    # def test_number2(self):
    #     assert False


if __name__ == '__main__':
    pytest.main(['-s', '--html=./report/result.html', '-—alluredir=./report'])
    # pytest.main(['-s', './testcase/test_search2.py', '--alluredir', './report/xml'])
    os.system('allure gengerate ./report/xml -o ./allreport --clean')
