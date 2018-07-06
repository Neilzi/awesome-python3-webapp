#! /usr/bin/env python
# -*- coding:utf-8 -*-

from coroweb import get, post
from orm import findAll
from models import User
import logging

@get('/')
async def index(request):
    users = findAll()
    # users = [User(name="小北", password="abcde", isadmin=1)]
    # users = [User(name="小北", password="abcde", isadmin=1)]
    logging.info('Users at handlers : \n%s ' % users)
    return {
        '__template__': 'test.html',
        'users': users
    }