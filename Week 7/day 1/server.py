# __Author__: Han
# __Date__: 2019/1/25

# socket参数：family（地址簇）, type（传输协议）
# # type=SOCK_STREAM: TCP
# # type=SOCK_DGRAM: UDP
# # family=AF_INET：服务器之间的通信，IPv4
# # family=AF_INET6：服务器之间的通信，IPv6
# # family=AF_UNIX：UNIX进程间的通信
# server下的方法：bind(), listen(), accept(), recv(), send(), sendall(), close()
# client下的方法：connect(), recv(), send(), sendall()，close()
# 其他方法：
# # setblocking(bool) 设置是否阻塞
# connect_ex(address), recvfrom(bufsize[, flag]), sendto(string[,flag],address),
# # settimeout(timeout), getpeername(), getsockname(), fileno()
import socket
sk = socket.socket()

print(sk)

address = ('127.0.0.1', 8000)

sk.bind(address)

sk.listen(3)    # 最大排队数，不能无限大，因为要在内核中维护连接队列
print('waiting..')

# conn, addr = sk.accept()     # 阻塞,
# OSError: [WinError 10057] 由于套接字没有连接并且(当使用一个 sendto 调用发送数据报套接字时)没有提供地址，发送或接收数据的请求没有被接受。

# conn, addr = sk.accept()     # 阻塞
#
# # ======================================================== #
# # 通信
#
# while True:
#     data = conn.recv(1024)      # 不允许发空，否则阻塞，直至发送不为空的数据过来
#     if not data:
#         conn.close()
#         conn, addr = sk.accept()
#         print(addr)
#         continue
#     print(str(data, 'utf8'))
#     inp = input('>>>')
#     conn.send(bytes(inp, 'utf8'))                  # 传送的类型需要是byte类型
#
# sk.close()

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
        inp = input('>>>')
        conn.send(bytes(inp, 'utf8'))                  # 传送的类型需要是byte类型

sk.close()



