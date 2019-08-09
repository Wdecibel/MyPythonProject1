# __Author__: Han
# __Date__: 2019/1/23


# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):   # 两个对象相加时，会自动执行第一个对象的__add__方法，将第二个对象当作参数传入
#         # return self.age + other.age
#         return Foo(self.name, other.age)
#
#     def __del__(self):          # 对象被销毁时，自动执行
#         print('析构方法')
#
#     # def __dict__(self):         # 将对象中封装的所有内容通过字典的形式返回
#     #     return 123
#
#
# obj1 = Foo('alex', 19)
# obj2 = Foo('eric', 66)
#
# r = obj1 + obj2
# print(r, type(r))


# class Foo:
#     '''
#     当前类
#     '''
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.n = 123
#
#
# ret = Foo.__dict__
# print(ret)


# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __getitem__(self, item):
#         print(item, type(item))
#
#     def __setitem__(self, key, value):
#         print(key, value)
#
#     def __delitem__(self, key):
#         print(key)
#
#
# li = Foo('alex', 18)
# print(li[1])                # 自动执行li对象类中的__getitem__方法，8当作参数传递给item
# print(li[1:8:2])            # 自动执行li对象类中的__getitem__方法，8当作参数传递给item
# # li[100] = 'adfa'
# # del li[999]

# __iter__


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        return iter([self])



li = Foo('alex', 18)
# list.__iter__()

for i in li:            # 执行li对象类Foo类中的__iter__方法，并获取其返回值；循环上一步返回的对象
    print(i)

























