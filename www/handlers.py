#! /usr/bin/env python
# -*- coding:utf-8 -*-

from coroweb import get
from orm import findAll

@get('/')
async def index(request):
    users = await findAll()
    return {
        '__template__': 'test.html',
        'user': users
    }