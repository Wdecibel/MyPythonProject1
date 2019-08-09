# __Author__: Han
# __Date__: 2019/1/18

# 继承：


# class GrandFather:
#     def drink(self):
#         print('GrandFather')
#         print(self)
#         pass
#
#     def drinks(self):
#         print('GrandFather')
#         print(self)
#         pass
#
#
# class Father(GrandFather):   # 父类，基类
#     def smoke(self):
#         pass
#
#     def drink(self):    # 重写
#         print('Father')
#         print(self)
#         # super(Father, self).drink()   # 同时执行，执行父类（基类）中的drink方法（推荐）
#         # GrandFather.drink(self)       # 同时执行，直接执行
#         pass
#
#     def tangtou(self):
#         pass
#
#
# class Son(Father):  # 子类，派生类
#     def baojian(self):
#         pass
#
#
# s = Son()
# s.baojian()
# s.drink()












