# coding = utf-8
'''
time:2021/9/18 15:32
'''
import time

import pytest
age = 18
class TestLogin:
    @pytest.mark.run(order=3)
    @pytest.mark.usermanage
    @pytest.mark.skipif(age >= 18,reason='已成年')
    def test_09_login(self):
        print("测试登录")

    @pytest.mark.run(order=1)
    def test_02_resourcess(self):
        print("测试资源")

    @pytest.mark.run(order=4)
    def test_03_class(self):
        print("测试课堂")
        assert 1==2

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @pytest.mark.usermanage
    def test_06_homework(self):
        print("测试作业")