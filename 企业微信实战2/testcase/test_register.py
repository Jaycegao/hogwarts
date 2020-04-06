#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from selenium import webdriver

from 企业微信实战2.page.index import Index


class TestRegister:
    def setup(self):
        # 初始化index
        self.index = Index()

    def test_register(self):
        # 从index中进入注册页，完成输入
        self.index.goto_register().register()
