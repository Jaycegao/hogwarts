#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
from python.calc import Calc
import pytest

class calc:
    def setup(self):
        self.calc = Calc()
    def test_add(self):
        assert self.calc.add(1, 2) == 3

    def test_div(self):
        assert self.calc.div(1, 2) == 0.5


if __name__ == '__main__':
    pytest.main()
