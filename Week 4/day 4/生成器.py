# __Author__: Han
# __Date__: 2019/1/9

# s = [x*2 for x in range(100000)]

# l = [1, 2, 3]
# a = l[1]
# b = l[2]

# s = (x*2 for x in range(10))

# print(s)    # <generator object <genexpr> at 0x0000021621D7C4C0>
#
# print(next(s))  # 等价于s.__next__()
#
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))  # StopIteration

# 生成器就是一个可迭代对象(Iterable)
# for i in s:
#     print(i)

# 生成器一共两种创建方式
# 1 (x*2 for x in range(5))
# 2 yield


# def foo():
#     print('ok')
#     yield 1
#
#     print('ok2')
#     yield 2
#
#     return None
#
#
# g = foo()
# print(g)    # <generator object foo at 0x000001DEB9F0C4C0>

# next(g)
# a = next(g)
# b = next(g)
# print(a, b)

# for i in foo():
#     print(i)

# 什么是可迭代对象（拥有__iter__方法的）
# l = [1, 2, 3]
# l.__iter__()
#
# t = (1, 2, 3)
# t.__iter__()
#
# d = {'name':'123'}
# d.__iter__()


# def fib(max):
#     n, before, after = 0, 0, 1
#     while n < max:
#         yield before
#         before, after = after, before + after
#         n += 1
#
#
# g = fib(8)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def bar():
#     print('ok1')
#     count = yield 1
#     print(count)
#
#     yield 2


# b = bar()
# b.send(None)    # next(b)
# print(s)
# t = b.send('eee')
# print(t)
# b.send('fff')



