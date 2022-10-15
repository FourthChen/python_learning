# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 11:30
# @Author  : sihao
# @File    : 4-socket和线程配合.py
import socket
import threading
import time
def task(conn):
    time.sleep(10)
    data=conn.recv(1024)
    print(data)
    conn.close()
server=socket.socket()

server.bind(('192.168.13.84',8001,))
server.listen(5)

while True:
    conn,addr=server.accept()
    t=threading.Thread(target=task,args=(conn,))
    t.start()