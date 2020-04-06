#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from time import sleep

from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestScroll():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("http://www.baicu.com")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touch(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.XPATH, "//*[@id='kw']").send_keys("selenium_3")
        ele = self.driver.find_element(By.XPATH, "//*[@id='su']")
        action = TouchActions(self.driver)
        action.tap(ele)
        action.perform()
        action.scroll_from_element(ele, 0, 10000).perform()
        sleep(3)
