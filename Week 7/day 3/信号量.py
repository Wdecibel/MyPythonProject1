# __Author__: Han
# __Date__: 2019/1/31

# 并行锁，count = n，约束最多有n个线程同时工作
# 应用场景：数据库连接池上限

import threading, time


class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(5)
            semaphore.release()


if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)
    thrs = []
    for i in range(23):
        thrs.append(myThread())
    for t in thrs:
        t.start()









