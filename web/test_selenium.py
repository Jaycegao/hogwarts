#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from selenium import webdriver
from time import sleep

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    sleep(2)
