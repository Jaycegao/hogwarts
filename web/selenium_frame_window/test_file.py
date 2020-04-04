#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from time import sleep

from selenium.webdriver.common.by import By

from web.selenium_frame_window.base import Base


class TestFile(Base):
    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="sttb"]/img[1]').click()
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="uploadImg"]').send_keys("E:/Testing/image/1.jpg")
        sleep(3)
