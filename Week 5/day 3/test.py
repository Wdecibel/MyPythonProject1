# __Author__: Han
# __Date__: 2019/1/17

# dic = str({'1': '111'})
#
# f = open('test', 'w')
# f.write(dic)


with open('test', 'r') as f:
    data = f.read()
    print(eval(data)['1'])









