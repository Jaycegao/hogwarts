#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from selenium.webdriver.common.by import By

from selenium_3.page.basepage import BasePage


class AddMember(BasePage):
    # 添加成员页面实现输入内容并保存
    def add_member(self):
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("jayce")
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys("26033")
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys("18269857895")
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
