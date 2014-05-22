#coding=utf-8
__author__ = 'HuCC'

'''
在Python中，None、任何数值类型中的0、空字符串“”、空元组()、空列表[]、空字典{}都被当作False，
还有自定义类型，如果实现了__nonzero__()或__len__()方法且方法返回0或False，则其实例也被当作False，
其他对象均为True
'''
print bool(None)
print bool(0)
print bool('')
print bool(())
print bool({})
print bool([])

class TestBool():
    def __nonzero__(self):
        return False

    def __len__(self):
        return 0

print bool(TestBool())