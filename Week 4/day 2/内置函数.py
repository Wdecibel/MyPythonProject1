#__author__: Han
#__date__: 2019/1/3
#
# str = ['a', 'b', 'c', 'd']
#
# def fun1(s):
#     if s != 'a':
#         return s
#
# ret = filter(fun1, str) #(b,c,d)
# print(ret)  #<filter object at 0x000001E00F1BE940>
# print(list(ret))


# str = ['d', 'a', 'b']
# def fun2(s):
#     return s + 'alvin'
#
# ret = map(fun2, str)
# print(ret)
# print(list(ret))

# from functools import reduce
#
# def add1(x,y):
#     return x + y
#
# print(reduce(add1, range(1,10)))

lambda a ,b: a + b