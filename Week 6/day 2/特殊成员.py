# __Author__: Han
# __Date__: 2019/1/23

# 特殊成员


# class Foo:
#     def __init__(self):
#         print('init')
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#
#
# # obj = Foo()
# # obj()
# Foo()()


class Foo:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __int__(self):  # int(对象)，自动执行对象的__int__方法，并将返回值赋值给对象
        return 111

    def __str__(self):   # istr(对象)，自动执行对象的__str__方法，并将返回值赋值给对象
        return 'alex'


obj = Foo()
print(obj, type(obj))   # print(str(obj))
print(obj, int(obj))
print(obj, str(obj))















