# __Author__: Han
# __Date__: 2019/1/29

# 一个线程就是一堆指令集合

# 并行：两个事情真正的同时在做
# 并发：

# CPU密集型任务：
# IO密集型任务：有状态，需要切换

import time
import threading

# begin = time.time()
#
#
# def foo(n):
#     print('foo:%s' % n)
#     time.sleep(1)
#     print('end foo')
#
#
# def bar(n):
#     print('bar:%s' % n)
#     time.sleep(2)
#     print('end bar')
#
#
# # foo(1)
# # bar(2)
# t1 = threading.Thread(target=foo, args=(1,))
# t2 = threading.Thread(target=bar, args=(2,))
# t1.start()
# t2.start()
#
# print('.....in the main......')
#
# t1.join()
# t2.join()
#
# end = time.time()
# print(end - begin)

begin = time.time()


def add(n):
    sum = 0
    for i in range(n):
        sum += i
    print(sum)


# add(50000000)
# add(80000000)

t1 = threading.Thread(target=add, args=(50000000, ))
t1.start()

t2 = threading.Thread(target=add, args=(80000000, ))
t2.start()


t1.join()
t2.join()

end = time.time()
print(end - begin)


