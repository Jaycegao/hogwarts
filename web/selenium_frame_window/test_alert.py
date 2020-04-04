#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from web.selenium_frame_window.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element(By.XPATH, '//*[@id="draggable"]')
        drop = self.driver.find_element(By.XPATH, '//*[@id="droppable"]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(3)
        # 确认alert
        self.driver.switch_to.alert.accept()
        # 切换到默认frame
        self.driver.switch_to_default_content()
        self.driver.find_element(By.XPATH, '//*[@id="submitBTN"]').click()
        sleep(3)
