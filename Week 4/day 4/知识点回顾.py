# __Author__: Han
# __Date__: 2019/1/9

# 列表生成式
[x*2 for x in range(10)]

# 生成器（generator object）
# 创建生成器：
# 1.(x*2 for x in range(10))    >> generator object
# 2.def f():
#       yield
# f() >> generator object
# 生成器的方法：
# 1.next()
# 注意：生成器在创建的时候已经决定了能计算出值的个数，调用next的次数超过这个值就会报StopIteration错误
# 遍历所有元素可以通过for循环，三件事： 1.调用iter方法，返回迭代器；2.while循环调用next方法；3.
# while:
#     try:
#         i = next(list_Iterator)
#
#     except StopIteration:
#         break
# 2.send():
# f().send(None)    #等价于next(f())

# 迭代器：满足迭代器协议（__iter__(), __next__())

import time
time.time()
time.strftime()
time.gmtime()
time.localtime()
time.ctime()

import datetime
datetime.datetime.now()

import random
chr()
random.randrange
random.randint
random.choice
random.shuffle
