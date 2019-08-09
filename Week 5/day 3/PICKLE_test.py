# __Author__: Han
# __Date__: 2019/1/17

import pickle   # 可转换函数、类等对象，仅支持python，无法跨语言传递


def foo():
    print('ok')


data = pickle.dumps(foo)

with open('PICKLE_text', 'wb') as f:
    f.write(data)











