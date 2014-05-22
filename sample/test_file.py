# -*- coding: utf-8 -*-
import struct

_author__ = 'HuCC'

f = open('data.txt', 'a')
f.write('test succeeded')
f.close()

try:
    for line in open('data.txt', 'r'):
        print line
except:
    pass

with open('data.txt', 'r') as f:
    print f.read()



#将long型写入到文件中
bf = open('./data.dat','ab')
bf.write(struct.pack("L",123456789))
bf.close()

bf = open('./data.dat','rb')
#将读取的4个字节转换为long
print struct.unpack("l",bf.read(4))