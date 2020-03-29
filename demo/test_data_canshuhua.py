#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
import pytest


@pytest.mark.parametrize(["a", "b"], [(10, 20), (11, 20), (12, 20)])
class TestData:
    def test_data(self, a, b):
        print(a + b)
