#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''

from selenium.webdriver.common.by import By

from 企业微信实战2.page.basepage import BasePage
from 企业微信实战2.page.register import Register


class Index(BasePage):
    # 进入注册页
    def goto_register(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 点击立即注册按钮
        self.driver.find_element(By.XPATH, '//*[@id="tmp"]/div[1]/a[2]')
        # 进入到注册页
        return Register(self.driver)

    # 进入登陆页
    def goto_login(self):
        pass
