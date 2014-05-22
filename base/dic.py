# -*- coding: utf-8 -*-
__author__ = 'HuCC'

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

print a==b==c==d==e
print d

# for key in d.keys():
#     print 'key=%s, value=%s' % (key, d[key])

for key in d:
    print 'key=%s value=%s' % (key, d[key])

print d['one']

d[5] = 5
# print d.pop(5)

del d[5]
print d.get(5, '5 not found')

# fromkeys
d2 = {}.fromkeys(('x', 'y'), -1)
print 'fromkeys ', d2

#dict key value 互换
invert_d = dict([(v, k) for k, v in d.iteritems()])
print 'invert',invert_d

#list间隔转dict
list = [1, 2, 3, 4, 5, 6, 7, 8]
print 'list to dict ',dict(zip(list[::2], list[1::2]))

#字符串转dict
user = "{'name' : 'jim', 'sex' : 'male', 'age': 18}"
user_obj = eval(user)
print 'string to dict',type(user_obj), user_obj['sex']

