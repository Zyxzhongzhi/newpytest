# coding = utf-8
'''
time:2021/9/18 15:47
'''
'''
运行方式
1、主函数运行
2、命令行运行
3、读取pytest.ini配置文件(pytest单元测试框架的核心配置文件)
    位置：项目的根目录
    编码：必须是ANSI，可以使用notpad++修改编码格式
    作用：改变pytest默认的行为
    运行规则：主函数运行或命令行运行都会去读取配置文件
    
'''
import pytest

if __name__ == '__main__':
# 运行所有
    # pytest.main(['-s'])
    # pytest.main(['-v'])
    # pytest.main(['sv'])
# 指定模块运行
#     pytest.main(['-sv','test_product.py'])
# 指定目录
#     pytest.main(['-vs','./testcase'])
#通过nodeid指定用例运行，nodeid由模块名，分隔符(::)，类名，方法名，函数名组成。
    # pytest.main(['-vs', './interface_testcase/test_interface.py::test_04_func'])
    # pytest.main(['-vs', './interface_testcase/test_interface.py::TestInterface::test_03_interface'])

    # pytest.main(['-vs', './testcase','-n=2'])
    # pytest.main(['-vs', './testcase','--reruns=2','-x'])
    # pytest.main(['-vs', './testcase', '-x'])
    pytest.main(['-vs', './testcase', '--maxfail=2'])
    # pytest.main(['-vs', './testcase', '-k=ss'])

'''
-s ：表示输出调试信息
-v ：显示更详细信息，包括用例名、类名
-sv ：合并使用
-n ： 支持多线程或者分布式运行测试用例
--reruns num：失败用例重跑
-x ：只要有一个用例报错，测试立即停止
--maxfail=2：出现两个用例失败停止
-k：根据测试用例的部分字符串测试用例
--html ./report/report.html:生成html的测试报告
'''


'''unittest ascll的大小来绝对的执行的顺序
pytest 默认从上到下
改变默认的执行顺序：使用mark标记
@pytest.mark.run(order=2)
'''
