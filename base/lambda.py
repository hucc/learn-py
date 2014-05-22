# -*- coding: utf-8 -*-
_author__ = 'HuCC'


g = lambda x: x*2
print g(3)
print (lambda x: x*2)(3)
#内置函数
foo = [2, 18, 9, 22]

print filter(lambda x: x % 3 == 0, foo)

print map(lambda x: x * 2 + 10, foo)

print reduce(lambda x, y: x + y, foo)

