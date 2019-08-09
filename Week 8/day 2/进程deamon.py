# __Author__: Han
# __Date__: 2019/2/20

# 在脚本运行过程中有一个主线程，若在主线程中创建了子线程，当主线程结束时根据子线程daemon属性值的不同可能会发生下面的两种情况之一：
#
# 如果某个子线程的daemon属性为False，主线程结束时会检测该子线程是否结束，如果该子线程还在运行，则主线程会等待它完成后再退出；
#
# 如果某个子线程的daemon属性为True，主线程运行结束时不对这个子线程进行检查而直接退出，同时所有daemon值为True的子线程将随主线程一起结束，而不论是否运行完成。
#
# 属性daemon的值默认为False，如果需要修改，必须在调用start()方法启动线程之前进行设置。
# 另外要注意的是，上面的描述并不适用于IDLE环境中的交互模式或脚本运行模式，因为在该环境中的主线程只有在退出Python IDLE时才终止。

import time
from multiprocessing import Process


def foo(i):
    time.sleep(1)
    print(p.is_alive(), i, p.pid)
    time.sleep(1)


if __name__ == '__main__':
    p_list = []
    for i in range(10):
        p = Process(target=foo, args=(i,))
        # p.daemon = True
        p_list.append(p)

    for p in p_list:
        p.start()

    # for p in p_list:
    #     p.join()

    print('main process end')











