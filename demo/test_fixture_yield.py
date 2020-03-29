#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
import pytest


# 作用域：module是在模块执行之前，模块执行之后
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield
    print("执行teardown！")
    print("最后关闭浏览器")


def test_search1(open):
    print("test_search1")
    raise NameError
    pass


def test_search2(open):
    print("test_search2")
    pass


def test_search3(open):
    print("test_search3")
    pass


if __name__ == "__main__":
    pytest.main()
