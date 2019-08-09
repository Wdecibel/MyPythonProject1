# __Author__: Han
# __Date__: 2019/1/28

import subprocess

import socket
import os

sk = socket.socket()

print(sk)

address = ('127.0.0.1', 8000)

sk.bind(address)

sk.listen(3)
print('waiting..')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    conn, addr = sk.accept()
    print(addr)

    while True:
        data = conn.recv(1024)
        cmd, filename, filesize = str(data, 'utf8').split('|')
        path = os.path.join(BASE_DIR, 'upload', filename)
        filesize = int(filesize)

        f = open(path, 'ab')

        has_receive = 0
        while has_receive != filesize:
            data = conn.recv(1024)
            f.write(data)
            has_receive += len(data)
        f.close()

sk.close()











