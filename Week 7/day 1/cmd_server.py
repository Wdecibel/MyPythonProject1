# __Author__: Han
# __Date__: 2019/1/28

import subprocess

import socket

sk = socket.socket()

print(sk)

address = ('127.0.0.1', 8000)

sk.bind(address)

sk.listen(3)    # 最大排队数
print('waiting..')


while True:
    conn, addr = sk.accept()     # 阻塞
    print(addr)

    while True:
        try:
            data = conn.recv(1024)      # 不允许发空，否则阻塞，直至发送不为空的数据过来
        except ConnectionResetError:    # linux中不会报错，认为data为空
            break
        if not data:
            break
        print(str(data, 'utf8'))
        # obj = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
        obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)       # windows的shell默认用gbk编码
        cmd_result = obj.stdout.read()
        result_len = bytes(str(len(cmd_result)), 'utf8')
        conn.sendall(result_len)                        # 粘包现象：连续的两次发送时，第一部分大小太小则会等待，若后面有其他指令，则一并发送
        conn.recv(1024)                                 # 解决粘包的办法，加入recv分隔开，但需要改动client端
        # inp = input('>>>')
        # conn.send(bytes(inp, 'utf8'))                  # 传送的类型需要是byte类型
        conn.sendall(cmd_result)

sk.close()











