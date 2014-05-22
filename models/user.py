# -*- coding: utf-8 -*-
_author__ = 'HuCC'

import post


class User:
    def __init__(self, username, password='123456'):
        self.id = 1
        self.username = username
        self.password = password

    def update(self,password):
        self.password=password


    def do_post(self,p):
        p.update(p.title,p.content)



p=post.Post('testtitle', 'testcontent', None, None)
u=User("test")
u.do_post(p)