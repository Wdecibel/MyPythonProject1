# __Author__: Han
# __Date__: 2019/1/30

import time
import threading


# def music(func):
#     for i in range(2):
#         print('I was listening to %s. %s' % (func, time.ctime()))
#
# def move(func):
#     for i in range(2):
#         print('I was at the %s! %s' % (func, time.ctime()))
#
#
# if __name__ == '__main__':
#     music(u'七里香')
#     move(u'世界末路')

def music(func):
    print(threading.current_thread())
    for i in range(2):
        print('Begin listening to %s. %s' % (func, time.ctime()))
        time.sleep(2)
        print('End listening to %s. %s' % (func, time.ctime()))


def move(func):
    print(threading.current_thread())
    for i in range(2):
        print('Begin at the %s %s' % (func, time.ctime()))
        time.sleep(3)
        print('End at the %s %s' % (func, time.ctime()))


threads = []
t1 = threading.Thread(target=music, args=('七里香', ))
threads.append(t1)
t2 = threading.Thread(target=move, args=('阿甘正传', ))
threads.append(t2)

if __name__ == '__main__':
    # music(u'七里香')
    # move(u'世界末路')

    for t in threads:
        t.setDaemon(True)           # 守护线程：如果主线程结束，子线程自动结束
        t.start()
    t2.join()
    print(threading.current_thread())
    print(threading.active_count())
    print('all over %s' % time.ctime())






