# __Author__: Han
# __Date__: 2019/1/30

import threading
import time

# def foo(n):
#     pass
#
#
# t1 = threading.Thread(target=foo, args=(1,))
# t1.start()


class MyTread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print('running on number: %s' % self.num)
        time.sleep(3)


if __name__ == '__main__':
    t1 = MyTread(1)
    t2 = MyTread(2)
    t1.start()
    t2.start()




