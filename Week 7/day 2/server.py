import socketserver


class MyServer(socketserver.BaseRequestHandler):        # 必须继承的类方法，且必须重写一个类

    def handle(self):                                   # 重写父类方法，父类中为pass
        print('server starting...')
        while True:
            conn = self.request                         # client传过来的sk对象
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data, 'utf8'))
                print('waiting...')
                server_response = input('>>>')
                conn.sendall(bytes(server_response, 'utf8'))
            conn.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8091), MyServer)
    server.serve_forever()
    # server.handle_request()












