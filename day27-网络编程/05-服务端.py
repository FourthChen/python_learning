
import socket

server=socket.socket()

server.bind(('127.0.0.1',8001))

server.listen(5)

while True:
    conn,addr=server.accept()
    #字节类型
    while True:
        try:
            data=conn.recv(1024)  #阻塞
            if data==b'exit':
                print('关闭')
                break
            response=data+b'sb'
            conn.send(response)
        except Exception as e:
            break

    conn.close()