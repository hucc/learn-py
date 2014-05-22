# coding=utf-8
__author__ = 'hcc'
import commands
import os, sys

def getclasspath(app_lib_path):
    line = commands.getstatusoutput('ls ' + app_lib_path + '/*.jar')
    classpath = ''
    for lib in line[1].split('\n'):
        if lib.rstrip() == '':
            continue
        classpath = classpath + ':' + lib
    return classpath


def getprop(appinfo, getkey):
    value = ''
    file_object = open(appinfo)
    for line in file_object.xreadlines():
        line = line.rstrip()
        key = line.split('::')[0].strip()
        if cmp(key, getkey) == 0:
            value = line.split('::')[1]

    return value


def getpid(app_path):
    pid = ''
    try:
        file_object = open(app_path + '/pid')
        pid = file_object.read()
        pid = pid.strip()
        file_object.close()
    except Exception, ex:
        pid = ''
    return pid;


def getlogfile(app_path):
    return app_path + '/logs/app.log'


def start(app_path, mainclass, classpath, vmoptions, mainargs):
    print app_path + '[' + mainclass + '] check status ...'
    pid = getpid(app_path)
    if(pid == ''):
        print app_path + '[' + mainclass + '] check status ok\n'
        logfile = getlogfile(app_path)

        javaexec = 'nohup java ' + vmoptions + ' -cp '
        javaexec = javaexec + app_path + '/bin:'
        javaexec = javaexec + app_path + '/config'
        javaexec = javaexec + classpath
        javaexec = javaexec + ' ' + mainclass +' >'+ logfile + ' 2>&1 &' + ' echo $!> '+app_path+'/pid'
        print javaexec
        os.system(javaexec)
        print '\n'
        print app_path + '[' + mainclass + '] started ,pid:' + getpid(app_path) + '\n'
    else:
        print app_path + '[' + mainclass + '] has already  started !\n'


def startnl(app_path, mainclass, classpath, vmoptions, mainargs):
    print app_path + '[' + mainclass + '] check status ...'
    pid = getpid(app_path)
    if pid != '':
        print app_path + '[' + mainclass + '] check status ok\n'
        javaexec = 'nohup java ' + vmoptions + ' -cp ';
        javaexec = javaexec + app_path + '/bin:'
        javaexec = javaexec + app_path + '/config'
        javaexec = javaexec + classpath
        javaexec = javaexec + '' + mainclass +' '+mainargs+ '>/dev/null &' + ' echo $!> ' + app_path + '/pid'
        print javaexec
        os.system(javaexec)
        print '\n'
        print app_path + '[' + mainclass + '] started ,pid:' + getpid(app_path) + '\n'
    else:
        print app_path + '[' + mainclass + '] has already  started !\n'


def stop(app_path,mainclass):
    print app_path + '[' + mainclass + '] check status ...'
    pid = getpid(app_path)
    if pid != '':
        print app_path + '[' + mainclass + '] check status ok'
        os.system('kill -9 ' + pid)
        os.system('rm -rf ' + app_path + '/pid')
        print app_path + '[' + mainclass + '] stoped !\n'
    else:
        print app_path + '[' + mainclass + '] stop faild !\n'


def status(app_path):
    pid = getpid(app_path)
    if pid != '':
        print app_path + '[' + mainclass + '] is running !'
        print app_path + '[' + mainclass + '] pid: ' + pid + '\n'
    else:
        print app_path + '[' + mainclass + '] is not runing !\n'


def printinfo(app_path, manclass, vmoptions, mainargs):
    print '\n'
    print '#####################################################################################################################'
    print ' apppath:    ' + app_path
    print ' manclass:  ' + manclass
    print ' vmoptions: ' + vmoptions
    if mainargs!='':
        print ' mainargs: ' + mainargs
    pid = getpid(app_path)
    if pid != '':
        print ' pid:        ' + pid
    print '#####################################################################################################################'
    print '\n'


def printhelp():
    print 'Usage: javas apppath start|startnl|stop|restart|restartnl|status|info [mainargs]'
    print '     apppath            your app root path'
    print '     where opt is one of:'
    print '         start           start your app and log'
    print '         startnl         start your app not log'
    print '         stop            stop your app'
    print '         restart         restart your app and log'
    print '         restartnl       restart your app not log'
    print '         status          app is or not runnig'
    print '         info            pint app info'
    print '      mainargs           main args optional'
    print '\n'
    print '\n'

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        app_path = sys.argv[1];
        opt = sys.argv[2];

        appinfo = app_path + '/app.info'

        mainclass = getprop(appinfo, 'mainclass')
        
        mainargs=''
        if len(sys.argv) == 4:
            mainargs = sys.argv[3]
            
        vmoptions = getprop(appinfo, 'vmoptions')
        
        app_lib_path = app_path + '/lib'
        classpath = getclasspath(app_lib_path)

        if opt != 'info':
            printinfo(app_path, mainclass, vmoptions,mainargs)
        if opt == 'start':
            start(app_path, mainclass, classpath, vmoptions,mainargs)
        elif opt == 'startnl':
            startnl(app_path, mainclass, classpath, vmoptions,mainargs)
        elif opt == 'status':
            status(app_path)
        elif opt == 'stop':
            stop(app_path,mainclass)
        elif opt == 'restart':
            stop(app_path,mainclass)
            start(app_path, mainclass, classpath, vmoptions, mainargs)
        elif opt == 'restartnl':
            stop(app_path)
            startnl(app_path, mainclass, classpath, vmoptions, mainargs)
        elif opt == 'info':
            printinfo(app_path, mainclass, vmoptions, mainargs)
        else:
            print printhelp()

    else:
        print printhelp()