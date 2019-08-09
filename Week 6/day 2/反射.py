# __Author__: Han
# __Date__: 2019/1/25

# getattr, hasattr, setattr, delattr
# 通过字符串的形式，操作对象中的成员


# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         return '%s - %s' % (self.name, self.age)
#
#
# obj = Foo('alex', 18)

# # 用变量的值去取另一个变量的值
# b = 'name'
# print(obj.__dict__)
# print(obj.__dict__[b])
# print(getattr(obj, b))
#
# # 去某个地方获取值
# b = 'show'
# func = getattr(obj, b)
# print(func)
# print(func())

# # 判断对象中是否有某方法或属性hasattr
# print(hasattr(obj, 'name'))

# # 设置某方法或属性
# setattr(obj, 'k1', 'v1')    # 设置k1=v1，设置在内存中，class不变
# print(obj.k1)

# # 删除属性
# delattr(obj, 'name')
# print(obj.name)


# class Foo:
#     stat = '123'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         return '%s - %s' % (self.name, self.age)
#
#
# # 通过字符串的形式操作对象中的成员
# print(getattr(Foo, 'stat'))


# import s2       # 模块级别的反射
# print(s2.NAME)
# print(s2.func())

# print(getattr(s2, 'NAME'))
# print(getattr(s2, 'func')())
# print(getattr(s2, 'Foo'))

import s2
inp = input('请输入要查看的URL：')

if hasattr(s2, inp):
    func = getattr(s2, inp)
    result = func()
    print(result)
else:
    print('404')

























