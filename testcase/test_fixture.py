# coding = utf-8
'''
time:2021/9/23 11:05
'''
import pytest

'''
@pytest.fixture可实现部分以及全部用例的前置
@pytest.fixture(scope="",params="",autouse="",ids="",name="")
scope：表示的是被@pytest.fixture标记的方法的作用域：作用于function(默认)，class，module，package/session
params：参数化，支持list[],tuple(),字典列表[{},{},{}]，字典元组({},{},})
autouse：自动执行，默认False   (autouse=Ture时，自动使用)
ids：当使用params参数化时，给每一个值设置一个变量名，意义不大
name：给表示的是被@pytest.fixture标记的方法取一个别名
'''

# @pytest.fixture(scope="function")
# def my_fixture():
#     print('\n这是前置的方法，可实现部分以及全部用例的前置')
#     yield
#     print('\n这是后置的方法，可实现部分以及全部用例的后置')
#
# class Testcase:
#
#     def test_001(self):
#         print('\n001')
#
#     def test_002(self,my_fixture):
#         print('\n002')
#
# if __name__ == '__main__':
#     pytest.main()


# @pytest.fixture(scope="class",autouse='Ture')
# def my_fixture():
#     print('\n这是前置的方法，可实现部分以及全部用例的前置')
#     yield
#     print('\n这是后置的方法，可实现部分以及全部用例的后置')
#
# class Testcase1:
#
#     def test_001(self):
#         print('\n001')
#
#     def test_002(self,my_fixture):
#         print('\n002')
#
# class Testcase2:
#
#     def test_001(self):
#         print('\n003')
#
#     def test_002(self,my_fixture):
#         print('\n004')
# if __name__ == '__main__':
#     pytest.main()

# @pytest.fixture(scope="module",autouse='Ture')
# def my_fixture():
#     print('\n这是前置的方法，可实现部分以及全部用例的前置')
#     yield
#     print('\n这是后置的方法，可实现部分以及全部用例的后置')
#
# class Testcase1:
#
#     def test_001(self):
#         print('\n测试001')
#
#     def test_002(self,my_fixture):
#         print('\n测试002')
#
# class Testcase2:
#
#     def test_001(self):
#         print('\n测试003')
#
#     def test_002(self,my_fixture):
#         print('\n测试004')
# if __name__ == '__main__':
#     pytest.main()


# @pytest.fixture(scope="module",params=['成龙','李小龙','long'],ids=['cl','lxl','l'],name='aaaaa')
# # params=['成龙','李小龙','long']的params是参数名，有s
# # ids是将params重新命名
# # 当取了别名后，原来的名称不可使用
# def my_fixture(request):
#     print('\n这是前置的方法，可实现部分以及全部用例的前置')
#     yield request.param
#     print('\n这是后置的方法，可实现部分以及全部用例的后置')
#     # return request.param
#     # request.param是属性名，没有s
# #return 和 yield都表示返回，但return 后不能有代码，yield 返回后后面可接代码
#
#
# class Testcase1:
#
#     def test_001(self):
#         print('\n测试001')
#
#     def test_002(self,aaaaa):
#         print('\n测试002')
#         print('-----------'+str(aaaaa))
#
# class Testcase2:
#
#     def test_001(self):
#         print('\n测试003')
#
#     def test_002(self,my_fixture):
#         print('\n测试004')
# if __name__ == '__main__':
#     pytest.main()

'''
通过conftest.py 和 @pytest.fixture结合使用实现全局的前置应用（项目的全局登录，模块的全局处理）

conftest.py是单独存放的一个配置文件，不可更改名称
用处：可在不同的py文件中使用同一个conftest.py
conftest.py需要和运行的用例放至同一层，且不需要做任何的import导入操作
'''


class Testcase1:

    def test_001(self):
        print('\n测试001')

    def test_002(self,my_fixture):
        print('\n测试002')
        print('-----------'+str(my_fixture))

class Testcase2:

    def test_001(self):
        print('\n测试003')

    def test_002(self,my_fixture):
        print('\n测试004')
if __name__ == '__main__':
    pytest.main()
