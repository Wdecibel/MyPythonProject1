# __Author__: Han
# __Date__: 2019/2/20

# 进行进程间的通信
# from multiprocessing import Process, Queue
# import queue
#
# def f(q):
#     q.put([42, 2, 'hello'])     # name 'q' is not defined   子进程访问的q
#     print('subprocess q id:', id(q))
#
#
# if __name__ == '__main__':
#     # q = Queue()                 # 主进程创建的Queue
#     q = queue.Queue()
#     p_list = []
#     print('main q id:', id(q))
#
#     for i in range(3):
#         p = Process(target=f, args=(q,))        # 将q作为参数传入即可解决
#         p_list.append(p)
#         p.start()
#
#     print(q.get())
#     print(q.get())
#     print(q.get())
#
#     for i in p_list:
#         i.join()


# ==================================================================================

# from multiprocessing import Process, Pipe
# import os
#
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     print(conn.recv(), 'in the %s' % os.getpid())
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn, ))
#     p2 = Process(target=f, args=(child_conn, ))
#     p.start()
#     p2.start()
#     print(parent_conn.recv())       # [42, None, 'hello']
#     print(parent_conn.recv())
#     parent_conn.send('hello')
#     parent_conn.send('hello2')
#     p.join()







