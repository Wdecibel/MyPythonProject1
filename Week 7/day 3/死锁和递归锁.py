# __Author__: Han
# __Date__: 2019/1/31

import threading
import time


# class myThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def doA(self):
#         # lockA.acquire()
#         lock.acquire()
#         print(self.name, 'gotLockA', time.ctime())
#         time.sleep(3)
#         # lockB.acquire()
#         lock.acquire()
#         print(self.name, 'gotLockB', time.ctime())
#         # lockB.release()
#         lock.release()
#         # lockA.release()
#         lock.release()
#
#     def doB(self):
#         # lockB.acquire()
#         lock.acquire()
#         print(self.name, 'gotLockB', time.ctime())
#         time.sleep(2)
#         # lockA.acquire()
#         lock.acquire()
#         print(self.name, 'gotLockA', time.ctime())
#         # lockA.release()
#         lock.release()
#         # lockB.release()
#         lock.release()
#
#     def run(self):
#         self.doA()
#         time.sleep(0.01)            # CPU切换时间比调用时间慢
#         self.doB()
#
#
# if __name__ == '__main__':
#     # lockA = threading.Lock()
#     # lockB = threading.Lock()
#
#     lock = threading.RLock()                # 递归锁，可重用（包含一个计数器和一把锁）
#     threads = []
#     for i in range(5):
#         threads.append(myThread())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()


class Account:
    def __init__(self, id, money, r):
        self.balance = money
        self.id = id

    def withdraw(self, num):
        with r:
            self.balance -= num

    def repay(self, num):
        with r:
            self.balance += num

    def abc(self, num):
        with r:
            self.balance += num
            self.withdraw()


def transfer(_from, to, count, r):

    with r:
        _from.withdraw(count)
        to.repay(count)


r = threading.RLock()
a1 = Account('alex', 1000, r)
a2 = Account('xiaohu', 2000, r)

t1 = threading.Thread(target=transfer, args=(a1, a2, 100, r))
t2 = threading.Thread(target=transfer, args=(a2, a1, 200, r))

t1.start()
t2.start()
















