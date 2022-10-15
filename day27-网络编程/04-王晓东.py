
import socket
client=socket.socket()

#王晓东向服务端发起连接请求(递伞)
#阻塞，去链接，直到连接成功后才会继续向下走
client.connect(('10.104.3.215',8001))

#连接上服务端后，向服务端发送消息
client.send(b'hello')

#王晓东等待服务器给他发送消息
data=client.recv(1024)
print(data)

#关闭自己
client.close()