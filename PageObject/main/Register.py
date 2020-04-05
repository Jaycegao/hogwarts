#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from selenium.webdriver.common.by import By

from PageObject.main.basepage import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.XPATH, '//*[@id="corp_name"]').send_keys("hello")
        self.find(By.XPATH, '//*[@id="manager_name"]').send_keys("hello2")
        return True
