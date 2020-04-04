#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from selenium.webdriver.common.by import By

from web.selenium_frame_window.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # self.driver.switch_to.frame()
        self.driver.switch_to_frame("iframeResult")
        self.driver.find_element(By.XPATH, '//*[@id="draggable"]').click()
        # self.driver.switch_to_parent_frame()
        self.driver.switch_to_default_content()
        self.driver.find_element(By.XPATH, '//*[@id="submitBTN"]')
