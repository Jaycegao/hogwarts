#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from selenium.webdriver.common.by import By

from 企业微信实战2.page.basepage import BasePage


class Register(BasePage):
    # 填写表单
    def register(self):
        # 填写输入框
        self.driver.find_element_by_id("corp_name").send_keys("hello")
        self.driver.find_element_by_id("manager_name").send_keys("abcde")
