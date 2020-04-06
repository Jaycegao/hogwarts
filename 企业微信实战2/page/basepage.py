#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from selenium import webdriver


class BasePage:
    def __init__(self, driver=None):
        if driver is None:
            # 如果发现driver没有值，说明第一次实例化子类
            self.driver = webdriver.Chrome()
        else:
            # 如果发现有值，说明不是第一次实例化
            self.driver = driver
