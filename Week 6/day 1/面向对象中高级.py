# __Author__: Han
# __Date__: 2019/1/18

# 属性


# class Foo:
#     a = 'aaa'   # 保存在类中
#
#     def __init__(self, name):   # 默认参数保存在每份对象中
#         self.name = name        # 实例属性，且只能通过对象访问
#
#     def show(self):
#         print(self.name)
#
#
# print(Foo.a)    # 可直接访问类属性
# foo = Foo('a')
# print(foo.a)    # 也可通过对象简介访问类属性

# 方法：

class Foo:
    def bar(self):
        print('bar')

    @staticmethod               # 静态方法：加上装饰器，可直接从类调用
    def static_method():        # 静态方法self不是必须的
        print('123')

    @staticmethod
    def static_method2(a1, a2):
        print(a1, a2)

    @classmethod
    def classmd(cls):          # 类方法：至少应该有一个参数，由类直接调用，cls是指当前类
        print('classmd')



# Foo.static_method()
# Foo.static_method2(1, 2)
# Foo.bar(object)
# obj = Foo()
# obj.bar()

Foo.classmd()









