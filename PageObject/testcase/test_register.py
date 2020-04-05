#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from PageObject.main.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    # def teardown(self):
    #     self.main.quit()

    def test_register(self):
        assert self.main.goto_register().register()
