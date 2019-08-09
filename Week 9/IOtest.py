# __Author__: Han
# __Date__: 2019/3/5
import socket

# print(socket.socket())      # <socket.socket fd=516, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>

# fd文件描述符：一些设计底层的程序编写往往会围绕文件描述符展开

sk = socket.socket()

sk.bind()

sk.listen(3)

sk.accept()









