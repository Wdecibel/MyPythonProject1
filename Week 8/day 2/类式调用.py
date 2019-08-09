# __Author__: Han
# __Date__: 2019/2/14

from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        time.sleep(1)
        print('hello', self.name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = MyProcess()
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    print('end')











