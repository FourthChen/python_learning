# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 11:10
# @Author  : sihao
# @File    : socketserver模块.py

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        pass

server=socketserver.ThreadingTCPServer(('192.168.13.84',8001),MyServer)
server.serve_forever()