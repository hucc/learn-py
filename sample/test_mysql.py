# -*- coding: utf-8 -*-
_author__ = 'HuCC'

import MySQLdb

db = MySQLdb.connect("localhost","admin","admin","blogdb" )
# 使用cursor()方法获取操作游标
cursor = db.cursor()
try:
   cursor.execute("SELECT * FROM post")
   results = cursor.fetchall()
   for row in results:
      print row
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()
