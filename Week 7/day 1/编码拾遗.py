# __Author__: Han
# __Date__: 2019/1/28


# Py3只有两种数据类型：str, bytes

# str: unicode
# bytes: 十六进制

s = 'hello 世界'

print(type(s))          # <class 'str'>

# str -> bytes 编码
b = bytes(s, 'utf8')    # b'hello \xe4\xb8\x96\xe7\x95\x8c'
print(b)                # utf8 规则下的byte类型

b2 = s.encode('utf8')
# b2 = s.encode('gbk')
print(b2)

# bytes -> str 解码

# k = str(b2, 'gbk')
# print(k)                # hello 涓栫晫 （乱码）

# 解码方法一
k = str(b2, 'utf8')
print(k)                # str数据类型

# 解码方法二
k2 = b2.decode('utf8')
print(k2)

l2 = s.encode('gbk')
print('gbk编码下的bytes数据：', l2)













