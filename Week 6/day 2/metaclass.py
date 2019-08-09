# __Author__: Han
# __Date__: 2019/1/23

# python中一切事物都是对象


# class Foo:      # Foo类也是一个对象，都是type的对象
#     def function(self):
#         print(123)


# Foo = type('Foo', (object,), {'func': lambda x: 123})    # 声明了一个类，类中有一个成员func，等同于上面
# obj = Foo()
# print(obj)

class MyType(type):
    def __init__(self, what, bases=None, dict=None):
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj)


class Foo(object, metaclass=MyType):
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)


# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo()


