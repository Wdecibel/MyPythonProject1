# __Author__: Han
# __Date__: 2019/1/23

# 公有成员
# 私有成员：__字段名，只能间接访问，也无法通过继承访问


# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         # self.age = age
#         self.__age = age    # 私有，外部无法直接访问
#
#     def show(self):
#         return self.__age   # 通过函数间接访问
#
#
# obj = Foo('alex', 19)
# print(obj.name)
# print(obj.show())


# class Foo:
#     __v = '123'
#
#     def __init__(self):
#         pass
#
#     def show(self):
#         return Foo.__v
#
#     @staticmethod
#     def stat():
#         return Foo.__v
#
#
# obj = Foo()
# # print(obj.show())
# print(obj.stat())


# class Foo:
#     def __f1(self):
#         return 123
#
#     def f2(self):
#         return self.__f1()
#
#
# obj = Foo()
# ret = obj.f2()
# print(ret)

# class Father:
#     def __init__(self):
#         self.__gene = 123
#         self.gene = 123
#
#
# class Son(Father):
#     def __init__(self, name):
#         self.name = 123
#         self.__age = 18
#         super(Son, self).__init__()
#
#     def show(self):
#         print(self.name)
#         print(self.__age)
#         print(self.__gene)
#
# s = Son('alex')
# s.show()















