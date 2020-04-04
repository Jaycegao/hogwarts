#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from web.selenium_frame_window.base import Base


class TestWindows(Base):
    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="u1"]/a[8]').click()
        self.driver.find_element(By.XPATH, '//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])  # windows打印出来显示的是窗口是列表
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]').send_keys("username")
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__phone"]').send_keys("13820546951")
        sleep(2)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_10__userName"]').send_keys("dsahfdla")
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_10__password"]').send_keys("password")
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_10__submit"]').click()
        sleep(3)
