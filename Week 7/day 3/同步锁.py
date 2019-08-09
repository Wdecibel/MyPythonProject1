# __Author__: Han
# __Date__: 2019/1/30

# 同步锁对特定代码块上锁，且为串行
import threading
import time


def addNum():
    global num
    # num -= 1

    r.acquire()
    temp = num
    print('--get num:', num)
    print('--get num:', num)
    print('--get num:', num)
    num = temp - 1              # 线程冲突，CPU时间
    r.release()


num = 100   # 设定一个共享变量

thread_list = []

r = threading.Lock()            # 禁止CPU切换
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    # t.join()              # 完全变成串行
    thread_list.append(t)

for t in thread_list:       # 等待所有线程执行完毕
    t.join()

print('final num:', num)










