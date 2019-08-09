# __Author__: Han
# __Date__: 2019/2/19

from multiprocessing import Process
import os
import time


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())      # 父进程号
    print('process id:', os.getpid())           # 进程号


if __name__ == '__main__':                      # windows下必须加上此句
    info('\033[32;1mmain process line\033[0m')
    time.sleep(3)
    p = Process(target=info, args=('bob',))
    p.start()
    p.join()











