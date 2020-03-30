#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://home.testing-studio.com/")
        self.driver.implicitly_wait(10)  # 隐式等待

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]').click()

        # sleep(3)  # 直接等待
        '''
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1
'''
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
