__author__ = 'HUCC'
#-*- coding:utf-8 -*-

import psutil

def getpid(key):

    for i in psutil.get_process_list():
        # print len(i.cmdline()),i.cmdline()
        if len(i.cmdline())>0:

            for c in i.cmdline():
                if c.find(key)!=-1:
                    print i.cmdline()
                    return i.pid


if __name__=='__main__':
    pid=getpid('Chrome')
    print pid