
import socket

sk=socket.socket()

sk.connect(('127.0.0.1',8001))
while True:
    name=input("请输入姓名：")
    sk.send(name.encode('utf-8'))
    if name==b'exit':
        break
    response=sk.recv(1024)

    print(response.decode('utf-8'))

sk.close()