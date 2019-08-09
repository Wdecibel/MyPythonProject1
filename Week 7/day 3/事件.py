# __Author__: Han
# __Date__: 2019/1/31

# 事件：类似于condition，可以进行线程间的交互
# 含变量，event.isSet() == False将阻塞线程
# event.isSet()
# event.wait()
# event.clear()

import threading
import time




class Boss(threading.Thread):
    def run(self):
        print('BOSS：今晚大家都要加班到22:00。')
        event.isSet() or event.set()
        time.sleep(5)
        print('BOSS：<22：00>可以下班了。')
        event.isSet() or event.set()


class Worker(threading.Thread):
    def run(self):
        event.wait()
        print('Worker：哎……命苦啊！')
        time.sleep(1)
        event.clear()
        event.wait()
        print('Worker：OhYeah！')


if __name__ == '__main__':
    event = threading.Event()
    threads = []
    for i in range(10):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()




















