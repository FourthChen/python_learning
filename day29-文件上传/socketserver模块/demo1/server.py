# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 16:42
# @Author  : sihao
# @File    : server.py

import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        #字节类型
        while True:
            try:
                data = self.request.recv(1024)  # 阻塞
                if data == b'exit':
                    print('关闭')
                    break
                response = data + b'sb'
                self.request.send(response)
            except Exception as e:
                break
#1.创建socket对象  2.self.socket.bind()  3.self.socket.listen(5)
server=socketserver.ThreadingTCPServer(("127.0.0.1",8999),Myserver)
server.serve_forever()
