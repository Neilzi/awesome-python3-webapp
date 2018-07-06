#! /usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio, aiomysql
import logging; logging.basicConfig(level=logging.INFO)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User
from coroweb import get

engine = create_engine('mysql+mysqlconnector://awesome_mst:Tuniu520@localhost:3306/awesome')
DBSession = sessionmaker(bind=engine)


@asyncio.coroutine
def create_pool(loop, **kwargs):
    logging.info("create database connection pool...")
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kwargs.get('host', 'localhost'),
        port=kwargs.get('port', '3306'),
        user=kwargs.get('user'),
        password=kwargs.get('password'),
        db=kwargs['db'],
        charset=kwargs.get('charset', 'utf8'),
        autocommit=kwargs.get('autocommit', True),
        maxsize=kwargs('maxsize', 10),
        minsize=kwargs('minsize', 1),
        loop=loop
    )


@asyncio.coroutine
def select(sql, args, size=None):
    logging(sql + args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            result = yield from cur.fetchmany(size)
        else:
            result = yield from cur.fetchall()
        yield from cur.close()
        logging('rows returned: %s' % len(result))
        return result


# 执行增删改, 返回受影响的行数
@asyncio.coroutine
def execute(sql, args):
    logging(sql + args)
    global __pool
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor(aiomysql.DictCursor)
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected



def findAll():
    session = DBSession()
    users = session.query(User).order_by(User.id).all()
    logging.info(users)
    return users


if __name__ == '__main__':
    u = findAll()
    print(u)

