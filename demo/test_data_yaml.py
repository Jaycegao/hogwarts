#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
import pytest
import yaml


@pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open("./data.yaml")))
class TestData:
    def test_data(self, a, b):
        print(a + b)
