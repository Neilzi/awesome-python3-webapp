#! /usr/bin/env python
# -*- coding:utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
from jinja2 import Environment, FileSystemLoader


def index(request):
    return web.Response(body=b'<h1>Awesome!</h1>', content_type='text/html')

def init_jinja2(app, **kwargs):
    logging.info('init jinja2...')
    options = dict(
        autoescape = kwargs.get('autuescape', True),
        block_start_string = kwargs.get('block_start_string', '{%'),
        block_end_string = kwargs.get('block_end_string', '%}'),
        variable_start_string = kwargs.get('variable_start_string', '{{'),
        variable_end_string = kwargs.get('variable_end_string', '}}'),
        auto_reload = kwargs.get('auto_reload', True)
    )
    path = kwargs.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__), 'templates'))
    logging.info('Set jinja2 template path to %s .' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kwargs.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    init_jinja2
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info("Server start at http://127.0.0.1:9000")
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()