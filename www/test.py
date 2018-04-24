import orm
from models import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(loop, user='root', password='', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()
