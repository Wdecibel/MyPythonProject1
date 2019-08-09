#__author__: Han
#__date__: 2019/1/3

# def f():
#     print('ok')
#     return [1,2,3]  #结束函数且返回某个对象
# a = f()
# print(a)
# print(f())

def add(*args):
    # print(args)
    sum = 0
    for i in args:
        sum += i
    return sum
a = add(1,4)
print(a, end='')

def foo():
    return 1, '123', [1,2,3]
print(foo())

# 1、函数默认返回None
# 2、return多个对象，会封装为一个对象