#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
import json
from time import sleep
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWeChat():
    def setup(self):
        # chrome启动时属性的类，复用浏览器
        # 声明一个变量，设置为chromeoptions
        c_options = webdriver.ChromeOptions()
        # 设置debug模式相同的端口号
        c_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH, '//*[@id="indexTop"]/div[2]/aside/a[1]')

    def teardown(self):
        self.driver.quit()

    def test_wechat(self):
        # self.driver.get("https://home.testing-studio.com")
        '''
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        sleep(3)
        '''
        # sleep(15)
        # cookies = self.driver.get_cookies()
        # # 写入cookies
        # with open("cookies.txt", "w") as f:
        #     json.dump(cookies, f)

        # 读取cookies
        with open("cookies.txt", "r") as f:
            cookies: List[Dict] = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
            sleep(3)
