# __Author__: Han
# __Date__: 2019/1/28
#
# import subprocess
#
# # 自己开了一个新的进程，与主进程无关，并行执行
# a = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE)     # PIPE把标准输出通过管道从子进程转到主进程，并封装到a对象中
# print(str(a.stdout.read(), 'gbk'))
#
# # print(a)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
# print(BASE_DIR)






