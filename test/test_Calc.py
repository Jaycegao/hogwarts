#!/usr/bin/env demo
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
import sys
import unittest

sys.path.append("..")
print(sys.path)
from python.calc import Calc


class test_Calc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calc()

    def test_add_1(self):
        self.assertEqual(3, self.calc.add(1, 2))

    def test_add_2(self):
        self.assertEqual(3, self.calc.add(0.01, 0.02))


if __name__ == '__main__':
    unittest.main()
