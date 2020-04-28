#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['paltformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
desired_caps['noReset'] = 'True'
desired_caps['dontstopAppOnReset'] = 'True'  # 首次启动的时候不停止app
desired_caps['skipDeviceInitialization'] = 'True'  # 跳过安装，权限设置等操作
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
driver.implicitly_wait(2)
driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
driver.back()
driver.back()
driver.quit()
