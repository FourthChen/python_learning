import socket

server=socket.socket()
ip_port=("127.0.0.1",8500)
server.bind(ip_port)

server.listen()
conn,addr=server.accept()

from_client_msg1=conn.recv(1024).decode("utf-8")

from_client_msg2=conn.recv(1024).decode("utf-8")

print("msg1:",from_client_msg1)
print("msg2:",from_client_msg2)


conn.close()
server.close()

#客户端

#由于第一次服务端接收数据的大小位1024B，导致剩余的976B的数据，在服务端第二次接受的数据中了
#根本原因：服务端不知道客户端发送了多少数据