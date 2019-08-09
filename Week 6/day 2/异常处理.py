# __Author__: Han
# __Date__: 2019/1/24

# while True:
#     try:
#         # 代码块，逻辑
#         i = int(input('请输入序号：'))
#     except Exception as e:          # Exception能捕获所有错误信息
#         # e是Exception对象，对象汇总封装了错误信息
#         # 上述代码块如果出错，自动执行当前块的内容
#         print(e)
#         i = 1
#     print(i)

# li = [11, 22]
# li[999]           # IndexError: list index out of range
# int('qwe')          # ValueError: invalid literal for int() with base 10: 'qwe'

# try:
#     # li = [11, 22]
#     # li[999]
#     int('wer')
#     print('若上面报错，此句不执行 ')
# except IndexError as e:
#     print('只能捕获IndexError', e)
# except ValueError as e:
#     print('只能捕获ValueError', e)
# except Exception as e:
#     print('所有报错都可捕获', e)
# else:                       # 若不报错，则执行
#     print('若不报错则执行...')
# finally:                    # 无论是否报错，都执行
#     print('无论是否报错，都执行...')


# try:
#     # int('adsf')
#     raise Exception('主动触发异常')   # 主动触发异常
# except Exception as e:
#     print(e)


# # 自定义异常，继承于Exception
# class abc(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return self.msg
#
#
# obj = abc('sadf')
# print(obj)


# # 断言assert
# print(123)
# assert 1==2         # 满足条件则执行，否则报错
# print(456)










