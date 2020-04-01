#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionsChains():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', 'false')
        self.driver = webdriver.Chrome(options=option)

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, "//*[@value='click me']")
        element_doubleclick = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
        elemet_rightclick = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        sleep(2)
        action.double_click(element_doubleclick)
        sleep(2)
        action.context_click(elemet_rightclick)
        sleep(2)
        action.perform()
        sleep(3)

    # 将光标移动到设置上
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    # 拖拽方法
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.XPATH, "//*[@id='dragger']")
        drop_element = self.driver.find_element(By.XPATH, "/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element, drop_element).perform()
        action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)

    # 输入数字
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        k1 = self.driver.find_element(By.XPATH, "/html/body/label[1]/input")
        k1.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


if __name__ == '__main__':
    pytest.main('-v', '-s', 'test_ActionChains.py')
