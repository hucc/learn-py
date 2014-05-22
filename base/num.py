#coding=utf-8
__author__ = 'HuCC'

i = 1
l = 22222222L
f = 12.1
f1 = float(i)
print f1



print abs(-1)
print pow(2, 5)
print round(3.55)

#
print hex(255)
print oct(255)
print bin(255)

#
print ord('a')
print chr(97)


'''
d: 有符号十进制整数
u: 无符号十进制整数
o: 无符号八进制整数
x: 无符号十六进制整数，a～f采用小写形式
X: 无符号十六进制整数，A～F采用大写形式
f: 浮点数
e，E: 浮点数，使用科学计数法
g，G:浮点数，使用最低有效数位
'''
print '2 is %x'%i

#
print coerce(1.0, 12L)
print divmod(10, 3)

