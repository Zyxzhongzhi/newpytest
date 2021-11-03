# coding = utf-8
'''
time:2021/9/18 16:03
'''
import pytest


def test_04_func():
    print("测试函数")

class TestInterface:
    @pytest.mark.smoke
    def test_03_interface(self):
        print("测试接口")