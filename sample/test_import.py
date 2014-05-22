# -*- coding: utf-8 -*-
_author__ = 'HuCC'
import toimport

import models1
import models1 as Base
from models1 import Person

from models import Post, User

#
toimport.to_import()


#
p = Post('testtitle', 'testcontent', None, None)
u = User("test")
u.do_post(p)


#
Base.check_status()
person=Person()
person.save()

person1=Base.Person()

person2=models1.Person
