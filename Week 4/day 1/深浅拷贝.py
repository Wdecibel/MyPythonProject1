#__author__: Han
#__date__: 2019/1/3

# s = [1, 'alex', 'alvin']
#
# s1 = [1, 'alex', 'alvin']
# s1[0] = 2
# print(s)
# print(s1)
# s = [1, 'alex', 'alvin']

# s2 = s.copy()
# print(s2)
# s2[0] = 3
# print(s)
# print(s2)
s = [[1,2], 'alex', 'alvin']
s3 = s.copy()
print(s3)

# s3[1] = 'linux'
# print(s)
s3[0][1]=3
print(s3,s)
print(id(s))
print(id(s3))