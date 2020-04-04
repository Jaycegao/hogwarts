#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from time import sleep

from selenium.webdriver.common.by import By

from web.selenium_frame_window.base import Base

import pytest


class TestJS(Base):
    @pytest.mark.skip
    def test_js(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("selenium")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=100000")
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="page"]/a[10]').click()
        sleep(3)
        # for code in [
        # 'return document.title','JSON.stringify(performance.timing)'
        # ]:
        print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        element_time = self.driver.execute_script(
            "a= document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-05-01'")
        sleep(3)
        print(self.driver.execute_script("document.getElementById('train_date').value"))
        print(element_time)
