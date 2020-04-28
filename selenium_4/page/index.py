#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from time import sleep

from selenium.webdriver.common.by import By

from selenium_3.page.add_member import AddMember
from selenium_3.page.basepage import BasePage


class Index(BasePage):

    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        return AddMember(self.driver)

    def goto_import_address(self):
        pass
