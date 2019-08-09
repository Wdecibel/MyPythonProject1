# __Author__: Han
# __Date__: 2019/2/21

# import gevent
# import time
#
#
# def foo():
#     print('Running in foo', time.ctime())
#     gevent.sleep(1)             # 模拟I/O阻塞的情况
#     print('Explicit context switch to foo again', time.ctime())
#
#
# def bar():
#     print('Explicit context to bar', time.ctime())
#     gevent.sleep(2)
#     print('Implicit context switch back to bar', time.ctime())
#
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])


from gevent import monkey
monkey.patch_all()              # 遇到I/O阻塞后可立刻切换，监听度更好
import gevent
from urllib.request import urlopen
import time


def f(url):
    print('Get: %s' % url)
    resp = urlopen(url)
    data = resp.read()

    print('%d bytes received from %s.' % (len(data), url))


# l = ['https://www.python.org/', 'https://www.yahoo.com/', 'https://github.com']
start = time.time()
# for url in l:
#     f(url)


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com'),
])

print(time.time() - start)














