#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import functools
import logging; logging.basicConfig(level=logging.INFO)


def get(path):
    '''
    Define decorator @get('/path')
    :param path: url path
    :return: decorator
    '''
    def decorator(func):
        functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.info('Call function %s .' % func.__name__)
            return func(*args, **kwargs)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator