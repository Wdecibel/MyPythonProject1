# __Author__: Han
# __Date__: 2019/1/25


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


# obj = Foo()         # obj对象，也是Foo类的实例，实例化
# obj1 = Foo()
# obj2 = Foo()
# obj3 = Foo()

# # 单例模式：
# # 单例，单个实例，永远使用同一份实例（对象）；
# # 模式

class Foo:

    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v










