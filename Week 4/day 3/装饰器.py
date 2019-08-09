# __author__: Han
# __date__: 2019/1/7
import time


# 功能函数加参数
def logger(flag='False'):
    def display_time(func):
        def inner(*x, **y):
            start = time.time()
            func(*x, **y)
            end = time.time()
            print('spend %s' % (end - start))
            if flag == 'True':
                print('日志记录')
        return inner
    return display_time


@logger('True')   # @display_time
def add(*a, **b):
    sum1 = 0
    for i in a:
        sum1 += i
    print(sum1)
    time.sleep(1)


@logger()   # bar = display_time(bar)
def bar():
    print('bar...')
    time.sleep(3)


add(1, 3, 5, 7, 9)   # 执行inner函数

bar()


# 装饰器加参数


