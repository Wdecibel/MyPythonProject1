# __Author__: Han
# __Date__: 2019/1/17


import pickle


# 必须调用双方都有函数内容才可以
def foo():
    print('ok')


with open('PICKLE_text', 'rb') as f:
    data = f.read()
    data = pickle.loads(data)
data()
# print(data['name'])










