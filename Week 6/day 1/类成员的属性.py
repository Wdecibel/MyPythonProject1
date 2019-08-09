# __Author__: Han
# __Date__: 2019/1/21


# class Foo:
#     def __init__(self):
#         self.name = 'a'
#         # obj.name
#     # obj.bar()
#     def bar(self):
#         # self是对象
#         print('bar')
#
#     # 用于执行obj.per
#     @property
#     def per(self):      # 属性、特性
#         print('123')
#         return 1
#
#     # 用于执行obj.per = 123
#     @per.setter
#     def per(self, val):
#         print(val)
#
#     # 删除
#     @per.deleter
#     def per(self):
#         print('666')
#
#
# obj = Foo()
# r = obj.per     # 按照字段一样调用，property
# print(r)
# obj.per = 123   # setter
#
# del obj.per     # deleter

class Foo:
    def f1(self):
        return 123

    def f2(self, v):
        print(v)

    def f3(self):
        print('del')

    per = property(fget=f1, fset=f2, fdel=f3, doc='I am a property')

    # @property
    # def per(self):
    #     return 123


obj = Foo()

# ret = obj.per
# print(ret)

obj.per = 123456

del obj.per









