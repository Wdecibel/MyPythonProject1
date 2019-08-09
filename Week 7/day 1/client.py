# __Author__: Han
# __Date__: 2019/1/25

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
    else:
        sk.send(bytes(inp, 'utf8'))                  # 传送的类型需要是byte类型
        data = sk.recv(1024)
        # sk.send(bytes('hah', 'utf8'))    # 阻塞
        print(str(data, 'utf8'))

sk.close()












