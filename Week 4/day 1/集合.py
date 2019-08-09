#__author__: Han
#__date__: 2019/1/3

a = set([1,2,3,4,5])
b = set([4,5,6,7,8])

# a = [1, 'www', 1, 1]
# print(a)

# s = set('alex li')
# s1 = ['alvin', 'ee', 'alvin']
# print(set(s1))
# print(s)

# s = {2, 3, 'alex'}
# print(s)
# s.update([12,'eee'])
# print(s)

# s.remove(2)
# s.pop()
# s.clear()
# print(s)

# print(set('alex') == set('alexexexe'))
# print(set('alex')<=set('alex'))

# print(a and b)
# print(a or b)
#
# print(a.intersection(b))
# print(a & b)
#
# print(a.union(b))
# print(a | b)
#
# print(a.difference(b))  #in a but no in b
# print(a-b)
#
# print(a.symmetric_difference(b))    #对称差集
# print(a^b)

# print(a.issuperset(b))  #父集 超集
# print(a>b)
# print(a.issubset(b))    #子集
# print(a<b)

# 主要的原因是 & ！= and , | != or
# python 中 & 、| 代表的是位运算符， and 、or代表的是逻辑运算符
# ① 当 a and b的结果为True 的时候，返回的并不是True，而是 运算结果的最后一位变量的值。这里是 返回b的值
# （b and a 为真 ，返回的是 a 的值）,
# 当a and b结果为False 的时候，返回的是第一个False 的值，如 a 和 b都为False 那么返回 a的 值
# ，a 为 真， b 为假，那么返回的是 b的值
#
# ②当 a or b 为真的时候，返回的是第一个真的变量的值，如，当a 和 b都为真，那么返回的是 a
# 若 a or b 假的时候，返回的是最后一个判断条件的值，这里返回的是 b 的值
#
# 所以上面的代码 a and b返回的是 b的值  {4, 5, 6, 7, 8}
# a or b 返回的则是 a 的值 {1, 2, 3, 4, 5, 6, 7, 8}





