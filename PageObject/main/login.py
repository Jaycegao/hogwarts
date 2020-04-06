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


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.XPATH, '//*[@id="wework_admin.loginpage_wx_$"]/page/div[2]/a').click()
        return Register(self._driver)
