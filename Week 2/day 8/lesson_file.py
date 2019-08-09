#__author__: Han
#__date__: 2018/11/15


f = open("小重山", "r+", encoding="utf-8")

# data = f.read(5)
# print(data)
number = 0
for line in f:
    number += 1
    if number == 6:
        f.write("alex")

f.write()

f.close()