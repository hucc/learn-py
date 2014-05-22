#coding=utf-8
__author__ = 'HuCC'

# 去空格及特殊符号
s = ' 123456 '
print 'trim',s.strip().lstrip().rstrip(',')


# 连接字符串
s1 = 'append'
s += s1
print '+',s

# 查找字符
print 'index',s.index('1')

# 比较字符串
s1 = 'strchr'
print 'cmp',cmp(s, s1)


# 字符串长度
#strlen(sStr1)
print 'len',len(s)

# 将字符串中的大小写转换
print 'upper',s.upper()

# 追加指定长度的字符串
#strncat(sStr1,sStr,n)
s1 += s1[0:3]
print 'split ',(s1)

# 字符串指定长度比较
#strncmp(sStr1,sStr,n)
s2 = 'append'
print cmp(s1[0:3], s2[0:3])

# 将字符串前n个字符替换为指定的字符
print 3 * 'x' + s1[3:]

# 翻转字符串
print 'revert',s,s[::-1]

# 查找字符串
print 'find ',s1.find('a')

# 分割字符串
print 'ab,cde,fgh,ijk'.split(',')


li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print s
print s.split(';')

