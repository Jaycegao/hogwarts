#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # 参数中的drivr要指定类型才能识别到
    def __init__(self, driver: WebDriver = None):
        # 让python编译器知道有一个实例变量
        self.driver = None
        if driver is None:
            # 复用浏览器,如果driver是空，就复用  chrome -remote-debugging-port=9222
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opts)
            # 隐式等待
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver
