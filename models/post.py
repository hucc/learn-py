# coding: utf-8

import time


class Post():
    #公有静态属性,只能通过类来操作类属性。
    count = 0
    #私有静态属性
    __del_count = 0

    def __init__(self, title, content, created_date=None, update_date=None):
        '''
        构造器
        '''
        self.id = 1
        self.title = title
        self.content = content
        self.update_date = update_date
        self.__status = self.update_date == None
        if created_date == None:
            self.created_date = time.time()
        else:
            self.created_date = created_date

        Post.count = Post.count + 1

    def update(self, title, content):
        '''
        实例方法,通过对象进行调用
        '''
        print 'id=%d update title=%s content=%s' % (self.id, title, content)

    def __test(self):
        '''
        私有方法,外边不能访问
        '''
        print self.__status


    @classmethod
    def cmethod(cls):
        '''
        类方法
        '''
        print 'say %s' % cls.count


    @staticmethod
    def smethod():
        '''
        静态方法，通过类进行调用
        '''
        print 'stat %d del %d' % (Post.count, Post.__del_count)


    def __repr__(self):
        '''
        类专有方法
        '''
        return '<Post %d %s>' % (self.id, self.title)


p = Post('testtitle', 'testcontent', None, None)
print p
p.update('1', '1')
print Post.count

p.cmethod()
p.smethod()
Post.cmethod()
Post.smethod()



'''
类的专有方法：
__init__  构造函数，在生成对象时调用
__del__   析构函数，释放对象时使用
__repr__ 打印，转换
__setitem__按照索引赋值
__getitem__按照索引获取值
__len__获得长度
__cmp__比较运算
__call__函数调用

__add__加运算
__sub__减运算
__mul__乘运算
__div__除运算
__mod__求余运算
__pow__称方
'''