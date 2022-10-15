# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 16:42
# @Author  : sihao
# @File    : client.py

import socket

sk=socket.socket()

sk.connect(('127.0.0.1',8999))
while True:
    name=input("请输入姓名：")
    sk.send(name.encode('utf-8'))

    response=sk.recv(1024)

    print(response.decode('utf-8'))

