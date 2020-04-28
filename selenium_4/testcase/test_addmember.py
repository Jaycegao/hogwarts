#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from time import sleep

from selenium_3.page.index import Index
import sys


class TestAddMember:
    def setup(self):
        self.index = Index()

    def test_add_member(self):
        # self.index.goto_add_member().add_member()
        # goto_add_member实例化了AddMember
        add_member = self.index.goto_add_member()
        # 添加成员
        add_member.add_member()
        sleep(2)
        # 测试是否添加
        assert add_member.get_first() == "jayce1"

# print(sys.path.append('Index'))
