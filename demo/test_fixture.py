#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
import pytest


def test_case1(login):
    print("test_case1,需要登录")
    pass


def test_case2():
    print("test_case2，不需要登录")


def test_case3(login):
    print("test_case3，需要登录")
    pass


if __name__ == '__main__':
    pytest.main()
