#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from python.calc import Calc


class calc:
    def test_add(self):
        calc = Calc()
        assert calc.add(1, 2) == 3
