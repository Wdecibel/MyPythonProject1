# __Author__: Han
# __Date__: 2019/1/31

# 遵循先进先出（FIFO），多线程利器，队列本身有一把锁；RabbitMQ（queue升级版）
# FIFO = queue.Queue
# LIFO = queue.LifoQueue
# Youxianji = queue.PriorityQueue
# 方法：q.qsize(), q.full(), q.empty()

import queue

d = queue.Queue(3)          # 超出则阻塞住，默认0（无限大）

d.put('jinxin')         # 插入数据
d.put('xiaohu')
d.put('haoran')         # put的block参数：默认为1（超出则阻塞），0
# d.put('haoran', 0)

# FIFO
print(d.get())          # 取出数据
print(d.get())
print(d.get())
print(d.get())          # queue.Empty


# import threading
# import time
#
# li = [1, 2, 3, 4, 5]
#
#
# def pri():
#     while li:
#         a = li[-1]
#         print(a)
#         time.sleep(1)
#         try:
#             li.remove(a)
#         except:
#             print('-----', a)
#
#
# t1 = threading.Thread(target=pri, args=())
# t2 = threading.Thread(target=pri, args=())
# t1.start()
# t2.start()

# import queue
# import threading
# import time
# from random import randint
#
#
# class Production(threading.Thread):
#     def run(self):
#         while True:
#             r = randint(0, 100)
#             q.put(r)
#             print('生产出来%s号包子' % r)
#             time.sleep(1)
#
#
# class Process(threading.Thread):
#     def run(self):
#         while True:
#             re = q.get()
#             print('吃掉%s号包子' % re)
#             time.sleep(1)
#
#
# if __name__ == '__main__':
#     q = queue.Queue(10)
#     threads = [Production(), Production(), Production(), Process()]
#
#     for t in threads:
#         t.start()












