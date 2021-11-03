# coding = utf-8
'''
time:2021/9/23 13:22
'''
import pytest


@pytest.fixture(scope="module")
def all_fixture(request):
    print('\n这是前置的方法，可实现部分以及全部用例的前置')
    yield request.param
    print('\n这是后置的方法，可实现部分以及全部用例的后置')