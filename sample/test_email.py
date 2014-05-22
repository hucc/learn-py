# -*- coding: utf-8 -*-
_author__ = 'HuCC'

import smtplib
from email.mime.text import MIMEText

mailto_list = ['quote_monitor@163.com']
mail_host = "smtp.163.com"  #设置服务器
mail_user = "quote_monitor@163.com"  #用户名
mail_pass = ""  #口令


def send_mail(to_list, sub, content):
    me = mail_user
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(mailto_list, "hello", "hello world！"):
        print "发送成功"
    else:
        print "发送失败"