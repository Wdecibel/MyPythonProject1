# __Author__: Han
# __Date__: 2019/1/30

import multiprocessing
import os


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = multiprocessing.Process(target=run_proc, args=('test',))
    print('Process will start.')
    p.start()
    p.join()
    print('Proecess end.')











