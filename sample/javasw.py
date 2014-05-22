# coding=utf-8
__author__ = 'hcc'
import psutil
import os, sys


def getprop(appinfo, getkey):
    value = ''
    file_object = open(appinfo)
    for line in file_object.xreadlines():
        line = line.rstrip()
        key = line.split('::')[0].strip()
        if cmp(key, getkey) == 0:
            value = line.split('::')[1]

    return value


def getpid(key):
    key=key.strip()
    for i in psutil.get_process_list():
        if len(i.cmdline()) > 0 and i.cmdline()[0].find('java') != -1:
            for c in i.cmdline():
                if c.find(key) != -1:
                    return i.pid
    return 0

def start(app_path, mainclass, vmoptions):
    javaexec = 'java ' + vmoptions + ' -cp '
    javaexec = javaexec + app_path + '/bin;'
    javaexec = javaexec + app_path + '/config;'
    javaexec = javaexec + app_path + '/lib/*;'
    javaexec = javaexec + ' ' + mainclass
    print javaexec
    print '\n'
    os.system(javaexec)


def stop(mainclass):
    pid = getpid(mainclass)
    if pid!=0:
        print mainclass+'[pid='+str(pid)+'] stop !'
        p = psutil.Process(pid)
        p.kill()

        print '\n'
    else:
        print mainclass+'[pid='+str(pid)+'] stop faild !'
        print '\n'



if __name__ == "__main__":
    if len(sys.argv) >= 3:
        app_path = sys.argv[1];
        opt = sys.argv[2];

        appinfo = app_path + '/app.info'
        mainclass = getprop(appinfo, 'mainclass')

        mainargs = ''
        if len(sys.argv) == 4:
            mainargs = sys.argv[3]

        vmoptions = getprop(appinfo, 'vmoptions')

        if opt == 'start':
            start(app_path, mainclass, vmoptions)
        elif opt == 'stop':
            stop(mainclass)
        elif opt == 'restart':
            stop(mainclass)
            start(app_path, mainclass, vmoptions)
        else:

            pass

    else:
        pass