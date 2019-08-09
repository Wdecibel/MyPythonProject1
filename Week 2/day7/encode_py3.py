#__author__: Han
#__date__: 2018/11/15

import sys
print(sys.getdefaultencoding())

s = "i am 特斯拉"
s_to_gbk = s.encode("gbk")
print(s)
print(s_to_gbk)