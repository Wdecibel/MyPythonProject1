# __Author__: Han
# __Date__: 2019/2/21

# 支持高并发
# 通过多进程利用多核

import time
import queue


def consumer(name):
    print('--->starting...')
    while True:
        new_baozi = yield                           # 有yield，是生成器
        print('[%s] is eating baozi %s' % (name, new_baozi))
        # time.sleep(1)


def producer():
    next(con)             # 执行consumer中yield之前的代码块
    next(con2)
    n = 0
    while n < 5:
        n += 1
        print('\033[32;1m[producer]\033[0m is making baozi %s' % n)
        con.send(n)
        con2.send(n)


if __name__ == '__main__':
    con = consumer('c1')            # 创建了一个生成器对象
    con2 = consumer('c2')
    p = producer()                  # 执行producer函数，p是函数的返回值




