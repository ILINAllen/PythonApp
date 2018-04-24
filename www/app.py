import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
from models import User, Blog, Comment
import orm
# import test

def index(request):
    return web.Response(body='<h1>Awesome</h1>')

def test(loop):
    yield from orm.create_pool(loop, user='root', password='', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    test(loop)
    # yield from orm.create_pool(loop, user='root', password='', database='awesome')
    #
    # u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    #
    # yield from u.save()
    logging.info('server started at http://127.0.0.1:9000...')

    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()