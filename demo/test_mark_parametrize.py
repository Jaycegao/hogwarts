#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
created on 2019-6-2
@author:Jayce Gao
project:
'''
import pytest
import sys


# 参数化，前两个变量，后面是对应数据
# 3+5-->test_input  8-->expect
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+5", 7), ("6*5", 35)])
def test_eval(test_input, expected):
    # eval 将字符串str当成有效的表达式来求值，并返回结果
    assert eval(test_input) == expected


# 参数组合
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [8, 10, 11])
def test_foo(x, y):
    print(f"测试数据组合x:{x},y:{y}")


# 方法名作为参数
test_user_data = ['Tome', 'Jerry']


@pytest.fixture(scope="module")
def login_r(request):
    # 这是接收并传入参数
    user = request.param
    print(f"\n 打开首页准备登陆，登陆用户：{user}")
    return user


# 标记结果
@pytest.mark.xfail
# skipif条件符合就跳过
# @pytest.mark.skipif(sys.platform == "win32", reason="不在macos上执行")
# @pytest.mark.skip("此次测试不执行登陆")
# indirect=True,可以把传过来的参数当作函数来执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值;{a}")
    assert a != ""
    raise NameError


if __name__ == "__main__":
    pytest.main()
