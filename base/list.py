# -*- coding: utf-8 -*-
__author__ = 'HuCC'
from math import pi

l1 = ['a', 1, ('aa', 'bb')]
l2 = list((1, 2, 3, 4))
l3 = range(1, 10)
l4 = [x ** 2 for x in range(10)]
'''
for x in range(10):
...     squares.append(x**2)
'''
l5=[x for x in l4 if x >= 5]
l5 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
'''
for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
'''

print l1
print l1[2][1]

if l1:
    print len(l1)

l1.append(5)  #追加元素
l1.insert(1, 5)
l1.pop(1)  #返回最后一个元素，并从list中删除之
l1.remove(1)  #删除第一次出现的该元素
l1.count(1)  #该元素在列表中出现的个数
print l1
l1.index(5)  #该元素的位置,无则抛异常
l1.extend([7, 8, 9])  #追加list，即合并list到L上
print l1
l1.sort()  #排序
l1.reverse()  #倒序

#opt
print l1 + ['one', 'two']
print l1 * 3

print [str(round(pi, i)) for i in range(1, 6)]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print  [[row[i] for row in matrix] for i in range(4)]


print 'zip', zip(*matrix)


l5=[1,2,3,4,5]
del l5[1:2]
print l5
del l5[:]#del l5
print l5
