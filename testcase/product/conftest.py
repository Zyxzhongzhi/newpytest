# coding = utf-8
'''
time:2021/9/23 13:22
'''
import pytest


@pytest.fixture(scope="module")
def product_fixture(request):
    print('\n这是商品管理前置')
    yield
    print('\n这是商品管理后置')