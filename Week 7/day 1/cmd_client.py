# __Author__: Han
# __Date__: 2019/1/28

import socket

sk = socket.socket()

print(sk)

address = ('127.0.0.1', 8000)
sk.connect(address)

# data = sk.recv(1024)    # 阻塞
while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))                     # 传送的类型需要是byte类型
    result_len = int(str(sk.recv(1024), 'utf8'))
    sk.sendall('111')                               # 解决粘包的方法
    print(result_len)                               # 打印数据长度

    data = bytes()
    while len(data) != result_len:
        recv = sk.recv(1024)
        data += recv
    # sk.send(bytes('hah', 'utf8'))                 # 阻塞
    # print(str(data, 'utf8'))
    print(str(data, 'gbk'))                         #

sk.close()











