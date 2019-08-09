# __Author__: Han
# __Date__: 2019/1/9

import random
# a = ['123', 4, [1, 2], 1]
# print(random.random())
# print(random.randint(1, 8))  # 包括1和8
# print(random.choice(a))
# random.shuffle(a)
# print(a)
#
# print(random.randrange(1, 3))


def v_code():
    code = ''
    for i in range(5):
        add = random.choice([chr(random.randrange(65, 91)), random.randrange(10)])
        # if i == random.randint(0, 3):
        #     add = random.randrange(10)
        # else:
        #     add = chr(random.randrange(65, 91))
        code += str(add)

    print(code)


v_code()

# print(chr(90))


