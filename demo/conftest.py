#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
import pytest


@pytest.fixture()
def login():
    print("这是个登录方法")
