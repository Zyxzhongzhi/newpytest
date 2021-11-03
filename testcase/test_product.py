# coding = utf-8
'''
time:2021/9/18 15:46
'''
import time

import pytest
# @pytest.mark.skip(reason="此条用例暂不执行")
# class TestProduct:
#     @pytest.mark.smoke
#     def test_02_product(self):
#         time.sleep(3)
#         print("测试产品")
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''使用fixture装饰器实现部分用例的前后置'''

class Testcase:
    def setup_class(self):
        print('在每个类执行前的初始化工作，比如：创建日志对象，创建数据库的连接，创建接口的请求对象')
    def setup(self):
        print("\n在执行测试用例之前初始化的代码：打开浏览器，加载网页")
    def test_001(self):
        print('\n001')

    def test_002(self):
        print('\n002')

    def teardown(self):
        print("\n在执行用例之后的扫尾的代码：关闭浏览器")

    def teardown_class(self):
        print('在每个类执行后的扫尾的工作:比如：销毁日志对象，销毁数据库的连接，销毁接口的请求对象')

if __name__ == '__main__':
    pytest.main()
