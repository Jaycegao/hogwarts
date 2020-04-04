#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
import os

from selenium import webdriver


class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == "forfox":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
