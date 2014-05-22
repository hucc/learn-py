# coding=utf-8
import fnmatch
import time
import datetime
import shutil
import zipfile


__author__ = 'hcc'
import os, sys

if __name__ == "__main__":
    curpath=os.path.abspath('.')
    parpath= os.path.abspath('../')
    os.system("mvn -f "+parpath+"/quote-core/pom.xml install -Dmaven.test.skip=true")
    os.system("mvn -f "+parpath+"/quote-block/pom.xml install -Dmaven.test.skip=true")
    os.system("mvn -f "+parpath+"/quote-data/pom.xml install -Dmaven.test.skip=true")

    os.system("mvn -f "+curpath+"/pom.xml package -Dmaven.test.skip=true")
    os.system("mvn -f "+curpath+"/pom.xml dependency:copy-dependencies -Dmaven.test.skip=true")

    deppath=curpath+"\\target\\dependency\\"
    deppathchg=curpath+"\\target\\dependency-change\\"

    if os.path.exists(deppathchg):
        shutil.rmtree(deppathchg)
    os.mkdir(deppathchg)

    zipfilename = curpath + "\\target\\dependency-change" + '.zip'
    if os.path.exists(zipfilename):
        os.remove(zipfilename)

    zipf=zipfile.ZipFile(zipfilename,'w',zipfile.ZIP_DEFLATED)

    time.sleep(2)

    for file in os.listdir(deppath):
        if fnmatch.fnmatch(file,'*.jar'):
            fileName = os.path.join(deppath, file)
            if time.time()-os.stat(fileName).st_mtime<=90:
                print fileName
                os.system('copy /y "'+fileName+'" "'+deppathchg+'"')
                zipf.write(fileName,arcname =os.path.split(fileName)[1] )

    pass

