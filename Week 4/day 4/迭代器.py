# __Author__: Han
# __Date__: 2019/1/9

# 生成器都是迭代器，迭代器不一定是生成器
# 迭代器：list，tuple, dict, string:  I
# 条件1. 有iter方法；2. 有next方法

# l = [1, 2, 3, 5]
# d = iter(l)  # l.__iter__()
# print(d)    # <list_iterator object at 0x000001E302E9A320>
#
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))

# for循环内部三件事：
# 1.调用可迭代对象的iter方法，返回一个迭代器对象；
# 2.连续调用迭代器对象的next方法
# 3.处理StopIteration
# for i in [1, 2, 3]:
#     iter([1, 2, 3])

# from collections import Iterator,Iterable
#
# print(isinstance([1, 2], list))
# l = [1, 2, 3, 5]
# d = iter(l)
# print(d)
# print(isinstance(l, list))
# print(isinstance(l, Iterable))
# print(isinstance(l, Iterator))
# print(isinstance(d, Iterator))

# f = open('abc.txt', 'r')
# for i in f:
#     print(i)

# 练习1：使用文件读取，找出文件最长的行？
max(len(x.strip()) for x in open('/hello/abc','r'))