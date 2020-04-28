#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['paltformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'  # 首次启动的时候不停止app
        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过安装，权限设置等操作
        desired_caps['unicodeKeyBoard'] = 'true'  # 设置可输入中文
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        '''
        1.打开雪球app
        2.打开输入框
        3.在搜索框输入“阿里巴巴”
        4.在搜索框里选择“阿里巴巴”，然后进行点击
        5.获取这只上阿里巴巴的股价，并判断这只股价大于200
        '''
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        time.sleep(3)
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        time.sleep(3)
        print(current_price)
        assert current_price > 200

    def test_attr(self):
        '''
        1.打开【雪球】应用首页
        2.定位首页的搜索框
        3.判断搜索框是否可用，并查看搜索框name属性值
        4.打印搜索框这个元素的左上角坐标和它的宽高
        4.向搜索框输入：alibaba
        5.判断【阿里巴巴】是否可见
        6.如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
        '''
        element = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        search_enabled = element.is_enabled()
        print(element.text)  # 元素属性
        print(element.location)  # 元素坐标
        print(element.size)  # 元素尺寸
        if search_enabled == True:
            element.click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
        element_alibaba = self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        # element_alibaba.is_displayed()
        element_display = element_alibaba.get_attribute("displayed")
        if element_display == 'true':
            print("搜索成功")
        else:
            print("搜索失败")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        # 方法1：通过坐标点
        # action.press(x=456, y=1000).wait(200).move_to(x=456, y=484).release().perform()
        # 方法2：获取当前屏幕尺寸
        widow_rect = self.driver.get_window_rect()
        width = widow_rect['width']
        height = widow_rect['height']
        x1 = width / 2
        y_start = height * 4 / 5
        y_end = height * 1 / 5
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_current(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        current_price = self.driver.find_element(*locator).text
        # print(f"当前09988对应的股票价格:{current_price}")
        assert float(current_price) > 200

    def test_myinfo(self):
        '''
        1.点击我的，进入到个人信息页面
        2.点击登陆，进入到登陆信息页面
        3.输入用户名密码
        4.点击登陆
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("请输入手机号")').send_keys("dsfdsa")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("dfssdfafds")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_croll_find_element(self):
        # 滚动查找元素
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("益学杨凯").instance(0));').click()


if __name__ == "__main__":
    pytest.main()
