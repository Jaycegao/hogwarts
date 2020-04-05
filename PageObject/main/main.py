#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from selenium.webdriver.common.by import By

from PageObject.main.Register import Register
from PageObject.main.basepage import BasePage
from PageObject.main.login import Login


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/?from=0010521013"

    def goto_register(self):
        self.find(By.XPATH, '//*[@id="tmp"]/div[1]/a[2]').click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.XPATH, '//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return Login(self._driver)
