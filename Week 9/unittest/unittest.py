# __Author__: Han
# __Date__: 2019/5/30

import unittest
from selenium import webdriver

class Ranzhi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()    # 选择Chrome浏览器


    def test_ranzhi(self):
        pass

    def tearDown(self):
        self.driver.quit()  # 退出浏览器











